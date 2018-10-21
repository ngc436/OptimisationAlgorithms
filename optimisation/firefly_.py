from optimisation import generate_population
from optimisation import Ackley, Michalewicz
import numpy as np
import math
import operator


# TODO: refactor function optimisation function call
class Firefly:

    def __init__(self, problem_dim, min_bound, max_bound):
        self.func = Michalewicz(problem_dim)
        self.position = generate_population(1, problem_dim, min_bound, max_bound)[0]
        self.brightness = None
        self.update_brightness()

    # the best fit is 0
    def update_brightness(self):
        self.brightness = -self.func.get_y(self.position)


class FireflyOptimizer:

    def __init__(self, **kwargs):
        self.population_size = int(kwargs.get('population_size', 10))
        self.problem_dim = kwargs.get('problem_dim', 2)
        self.min_bound = kwargs.get('min_bound', -5)
        self.max_bound = kwargs.get('max_bound', 5)
        self.generations = kwargs.get('generations', 10)
        self.population = self._population(self.population_size, self.problem_dim, self.min_bound, self.max_bound)
        self.gamma = kwargs.get('gamma', 0.97)  # absorption coefficient
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

    def step(self):
        self.population.sort(key=operator.attrgetter('brightness'), reverse=True)
        self._modify_alpha()
        tmp_population = self.population
        for i in range(self.population_size):
            for j in range(self.population_size):
                if self.population[i].brightness > tmp_population[j].brightness:
                    r = math.sqrt(np.sum((self.population[i].position - tmp_population[j].position) ** 2))
                    beta = (self.beta_init - self.beta_min) * math.exp(-self.gamma * r ** 2) + self.beta_min
                    tmp = self.alpha * (np.random.random_sample((1, self.problem_dim))[0] - 0.5) * (
                            self.max_bound - self.min_bound)
                    self.population[j].position = self.check_position(
                        self.population[i].position * (1 - beta) + tmp_population[
                            j].position * beta + tmp)
                    self.population[j].update_brightness()
        self.population[0].position = generate_population(1, self.problem_dim, self.min_bound, self.max_bound)[0]
        self.population[0].update_brightness()

    def run_firefly(self):
        for t in range(self.generations):
            print('Generation %s, best fitness %s' % (t, self.population[0].brightness))
            self.step()
        self.population.sort(key=operator.attrgetter('brightness'), reverse=True)
        return self.population[0].brightness, self.population[0].position

    def check_position(self, position):
        position[position > self.max_bound] = self.max_bound
        position[position < self.min_bound] = self.min_bound
        return position

    def _modify_alpha(self):
        delta = 1 - (10 ** (-4) / 0.9) ** (1 / self.generations)
        self.alpha = (1 - delta) * self.alpha
