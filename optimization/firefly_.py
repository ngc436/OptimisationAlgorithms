from .data_generator_ import *
from .benchmark_functions_ import Ackley
import numpy as np
import math


class FireflyOptimizer:

    def __init__(self, **kwargs):
        self.population_size = kwargs.get('population_size', 10)
        self.problem_dim = kwargs.get('problem_dim', 2)
        self.min_bound = kwargs.get('min_bound', -1)
        self.max_bound = kwargs.get('max_bound', 1)
        self.generations = kwargs.get('generations', 10)
        self.population = generate_population(population_size=self.population_size, problem_dim=self.problem_dim,
                                              min_bound=self.min_bound, max_bound=self.max_bound)
        self.base_beta = kwargs.get('base_beta', 1)
        self.gamma = kwargs.get('gamma', 1)
        self.alpha = kwargs.get('alpha', 0.2)

    def _error(self):
        raise NotImplementedError

    def run_firefly(self, verbose=1, gamma=0.95, optimization_benchmark='Ackley'):
        I = np.zeros(self.problem_dim)
        for ind, firefly in enumerate(self.population):
            I[ind] = self.Ackley(firefly)
        for t in range(self.generations):
            for i in range(self.population_size):
                for j in range(self.population_size):
                    if I[i] < I[j]:
                        compute_attractiveness()



            pass

    # TODO: implement me too
    def get_fitness(self):

        raise NotImplementedError


f_alg = FireflyOptimizer(population_size=100, problem_dim=10)
