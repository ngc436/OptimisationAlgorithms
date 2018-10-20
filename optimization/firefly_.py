from optimization import generate_population
from optimization import Ackley
import numpy as np
import math


# numpy.sqrt(numpy.sum((a-b)**2))

class Firefly:

    def __init__(self, problem_dim, min_bound, max_bound):
        self.func = Ackley(problem_dim)
        self.position = generate_population(1, problem_dim, min_bound, max_bound)[0]
        self.brightness = -self.func.get_y(self.position)
        # self.attractiveness =


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

    @staticmethod
    def _population(population_size, problem_dim, min_bound, max_bound):
        population = []
        for i in range(population_size):
            population.append(Firefly(problem_dim, min_bound, max_bound))
        return population

    def _error(self):
        raise NotImplementedError

    def run_firefly(self, verbose=1, gamma=0.95, optimization_benchmark='Ackley'):
        for t in range(self.generations):
            self.population = self.population.sort(key=lambda x: x.brightness)
            print('Generation %s, best fitness %s' % (t, self.population[0].brightness))
            for i in range(self.population_size):
                for j in range(self.population_size):
                    if self.population[i].brightness > self.population[j].brightness:
                        r = math.sqrt(sum((self.population[i].position - self.population[j].position) ** 2))
                        beta = (self.beta_init - self.delta) * math.exp((-self.gamma * r) ** 2) + self.delta
                        tmp = self.alpha*(np.random.random_sample((1, self.problem_dim)))*

                    #     compute_attractiveness()

    # TODO: implement me too
    def get_fitness(self):

        raise NotImplementedError


f_alg = FireflyOptimizer(population_size=100, problem_dim=10)
print(f_alg.population)
