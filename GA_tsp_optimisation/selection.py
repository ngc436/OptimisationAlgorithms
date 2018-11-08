import operator


class Selector:
    def __init__(self, selection_type):
        assert selection_type in ['roulette', 'tournament']
        self.selection_type = selection_type

    def selection(self, **kwargs):
        if self.selection_type == 'roulette':
            self._roulette(**kwargs)
        if self.selection_type == 'tournament':
            self._tournament(**kwargs)

    def _roulette(self, **kwargs):
        population = kwargs.get('population')
        overall_fitness = 0
        for individ in population:
            overall_fitness += individ.fitness
        for individ in population:
            individ._prob = individ.fitness / overall_fitness
        population.sort(key=operator.attrgetter('_prob'), reverse=True)

    def _tournament(self, **kwargs):
        raise NotImplementedError
