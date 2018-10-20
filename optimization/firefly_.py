from optimization import generate_population
from optimization import Ackley
import numpy as np
import math
import operator


class Firefly:

    def __init__(self, problem_dim, min_bound, max_bound):
        self.func = Ackley(problem_dim)
        self.position = generate_population(1, problem_dim, min_bound, max_bound)[0]
        self.brightness = self.update_brightness()

    def update_brightness(self):
        return -self.func.get_y(self.position)


class FireflyOptimizer:

    def __init__(self, **kwargs):
        self.population_size = kwargs.get('population_size', 10)
        self.problem_dim = kwargs.get('problem_dim', 2)
        self.min_bound = kwargs.get('min_bound', -1)
        self.max_bound = kwargs.get('max_bound', 1)
        self.generations = kwargs.get('generations', 10)
        self.population = self._population(self.population_size, self.problem_dim, self.min_bound, self.max_bound)
        self.delta = kwargs.get('delta', 0.97)  # randomness reduction
        self.gamma = kwargs.get('gamma', 1)  # absorption coefficient
        self.alpha = kwargs.get('alpha', 0.2)  # randomness [0,1]
        self.beta_init = kwargs.get('beta_init', 1)
        self.optimization_benchmark = kwargs.get('optimization_benchmark', 'Ackley')

    @staticmethod
    def _population(population_size, problem_dim, min_bound, max_bound):
        population = []
        for i in range(population_size):
            population.append(Firefly(problem_dim, min_bound, max_bound))
        return population

    def run_firefly(self):
        for t in range(self.generations):
            self.population.sort(key=operator.attrgetter('brightness'), reverse=True)
            print('Generation %s, best fitness %s' % (t, self.population[0].brightness))
            for i in range(self.population_size):
                for j in range(self.population_size):
                    if self.population[i].brightness > self.population[j].brightness:
                        r = math.sqrt(np.sum((self.population[i].position - self.population[j].position) ** 2))
                        beta = (self.beta_init - self.delta) * math.exp(-self.gamma * r ** 2) + self.delta
                        tmp = self.alpha * (np.random.random_sample((1, self.problem_dim)) - 0.5) * (
                                self.max_bound - self.min_bound)
                        self.population[i].position = self.population[i].position * (1 - beta) + self.population[
                            j].position * beta + tmp
                        self.population[i].update_brightness()

    # TODO: implement me too
    def get_fitness(self):

        raise NotImplementedError


f_alg = FireflyOptimizer(population_size=10, problem_dim=2, generations=100)
f_alg.run_firefly()
