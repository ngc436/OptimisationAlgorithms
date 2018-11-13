import operator
import random


class Selector:
    def __init__(self, selection_type):
        assert selection_type in ['roulette', 'tournament']
        self.selection_type = selection_type

    def selection(self, **kwargs):
        if self.selection_type == 'roulette':
            return self._roulette(**kwargs)
        if self.selection_type == 'tournament':
            return self._tournament(**kwargs)

    def yield_mating_pairs(self, pairs, population):
        for j in range(pairs):
            chosen = []
            for _ in range(2):
                selection_probability = random.random()
                for individ in population:
                    if selection_probability >= individ._prob:
                        chosen.append(individ)
                        break
            if len(chosen) < 2:
                chosen.append(population[-1])
                if len(chosen) == 1:
                    chosen.append(population[-2])
            yield chosen[0], chosen[1]

    def _roulette(self, **kwargs):
        population = kwargs.get('population')
        best_population = kwargs.get('best_perc')
        cumsum_fitness = 0
        for individ in population:
            cumsum_fitness += individ.fitness
            individ._prob = individ.fitness / cumsum_fitness
        return self.yield_mating_pairs(int(len(population) - int(len(population) * best_population))//2 + 1, population)

    def _tournament(self, **kwargs):
        raise NotImplementedError
