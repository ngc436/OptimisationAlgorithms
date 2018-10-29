import numpy as np
from data_utils import *


class Path:
    def __init__(self, path, fitness):
        self.path = path
        self.fitness = fitness


def _evaluate_fitness(path, coord):
    dist = 0
    for i in range(len(path)):
        if i == (len(path)-1):
            dist += np.linalg.norm(coord[path[0]] - coord[path[i]])
            break
        dist += np.linalg.norm(coord[path[i+1]] - coord[path[i]])
    return dist


def _generate_population(num_of_cities, population_size, coord):
    population = []
    min_so_far = 0
    for _ in range(population_size):
        path = np.random.permutation([i for i in range(num_of_cities)])
        fitness = _evaluate_fitness(path, coord)
        population.append(Path(path, fitness))
    return np.array(population)


# TODO: crossover and mutation
def ga_pipeline(coord=None, population_size=10, generations=10):
    num_of_cities = coord.shape[0]
    population = _generate_population(num_of_cities, population_size, coord)
    print(population)


coord = read_tsp_file('xqf131.tsp')
ga_pipeline(coord)
