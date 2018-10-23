import numpy as np

class Path:
    def __init__(self, path, fitness):
        self.path = path
        self.fitness = fitness

def _evaluate_fitness(path):
    raise NotImplementedError

def _generate_population(num_of_cities, population_size):
    population = []
    for _ in range(population_size):
        path = np.random.permutation([i for i in range(num_of_cities)])
        fitness = _evaluate_fitness(path)
        m = Path(path)
        population.append()
    return np.array(population)

def ga_pipeline(coord=None, population_size=10, generations=10):
    num_of_cities = coord.shape[0]


    raise NotImplementedError

_generate_population(131, 10)