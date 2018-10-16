from .data_generator_ import *
import numpy as np


class FireflyOptimizer:

    def __init__(self, **kwargs):
        self.population_size = kwargs.get('population_size', 10)
        self.problem_dim = kwargs.get('problem_dim', 2)
        self.min_bound = kwargs.get('min_bound', -1)
        self.max_bound = kwargs.get('max_bound', 1)
        self.generations = kwargs.get('generations', 10)
        self.population = generate_population(population_size=self.population_size, problem_dim=self.problem_dim,
                                              min_bound=self.min_bound, max_bound=self.max_bound)

    def run_firefly(self, verbose=1, gamma=0.95, optimization_benchmark='Ackley'):
        gamma = gamma
        I = np.zeros(self.problem_dim)
        for ind, firefly in enumerate(self.population):
            I[ind] = self.get_fitness(firefly)
        for t in range(self.generations):
            # TODO: implement me
            pass

    # TODO: implement me too
    def get_fitness(self):
        raise NotImplementedError
