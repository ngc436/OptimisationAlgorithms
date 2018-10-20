from optimization import generate_population
from optimization import Ackley
import numpy as np
import math
import operator


class Firefly:

    def __init__(self, problem_dim, min_bound, max_bound):
        self.func = Ackley(problem_dim)
        self.position = generate_population(1, problem_dim, min_bound, max_bound)[0]
        self.brightness = None
        self.update_brightness()

    # the best fit is 0
    def update_brightness(self):
        self.brightness = -self.func.get_y(self.position)


class FireflyOptimizer:

    def __init__(self, **kwargs):
        self.population_size = kwargs.get('population_size', 10)
        self.problem_dim = kwargs.get('problem_dim', 2)
        self.min_bound = kwargs.get('min_bound', -32)
        self.max_bound = kwargs.get('max_bound', 32)
        self.generations = kwargs.get('generations', 10)
        self.population = self._population(self.population_size, self.problem_dim, self.min_bound, self.max_bound)
        self.delta = kwargs.get('delta', 0.2)  # randomness reduction
        self.gamma = kwargs.get('gamma', 1)  # absorption coefficient
        self.alpha = kwargs.get('alpha', 0.25)  # randomness [0,1]
        self.beta_init = kwargs.get('beta_init', 1)
        self.beta_min = kwargs.get('beta_min', 0.2)
        self.optimization_benchmark = kwargs.get('optimization_benchmark', 'Ackley')

    @staticmethod
    def _population(population_size, problem_dim, min_bound, max_bound):
        population = []
        for i in range(population_size):
            population.append(Firefly(problem_dim, min_bound, max_bound))
        return population

    def run_firefly(self):
        for t in range(self.generations):
            self._modify_alpha()
            self.population.sort(key=operator.attrgetter('brightness'), reverse=True)
            tmp_population = self.population
            print('Generation %s, best fitness %s' % (t, self.population[0].brightness))
            for i in range(self.population_size):
                for j in range(self.population_size):
                    if self.population[i].brightness > tmp_population[j].brightness:
                        r = math.sqrt(np.sum((self.population[i].position - tmp_population[j].position) ** 2))
                        beta = (self.beta_init - self.beta_min) * math.exp(-self.gamma * r ** 2) + self.beta_min
                        tmp = self.alpha * (np.random.random_sample((1, self.problem_dim))[0] - 0.5) * (
                                self.max_bound - self.min_bound)
                        self.population[i].position = self.check_position(self.population[i].position * (1 - beta) + tmp_population[
                            j].position * beta + tmp)
                        self.population[i].update_brightness()

    def check_position(self, position):
        position[position > self.max_bound] = self.max_bound
        position[position < self.min_bound] = self.min_bound
        return position


    def _modify_alpha(self):
        delta = 1-(10**(-4)/0.9)**(1/self.generations)
        self.alpha = (1-delta)*self.alpha
