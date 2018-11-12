from data_utils import *
import operator
from GA_tsp_optimisation import Selector, Crossover, Mutation
from vis import *

coordinates = None


class Path:
    def __init__(self, path):
        self.path = path
        self.fitness = _evaluate_fitness(path)
        self._prob = None

    def update_path(self, new_path):
        self.path = new_path
        self.fitness = _evaluate_fitness(new_path)


def _evaluate_fitness(path):
    dist = 0
    for i in range(len(path)):
        if i == (len(path) - 1):
            dist += np.linalg.norm(coordinates[path[0]] - coordinates[path[i]])
            break
        dist += np.linalg.norm(coordinates[path[i + 1]] - coordinates[path[i]])
    if dist == 0:
        print(path)
    return dist


def _generate_population(num_of_cities, population_size):
    population = []
    for _ in range(population_size):
        path = np.random.permutation([i for i in range(num_of_cities)])
        population.append(Path(path))
        draw_path(path, coordinates)
    return population


# TODO: crossover and mutation
def ga_pipeline(coord=None, population_size=10, generations=10):
    num_of_cities = coord.shape[0]
    global coordinates
    coordinates = coord
    population = _generate_population(num_of_cities, population_size)
    s = Selector(selection_type='roulette')
    c = Crossover(crossover_type='ordered')
    # generations loop
    for _ in range(generations):
        pairs_generator = s.selection(population=population)
        new_generation = []
        for i, j in pairs_generator:
            child_1, child_2 = c.crossover(parent_1=i.path, parent_2=j.path)
            new_generation.append(Path(child_1))
            new_generation.append(Path(child_2))
        population = new_generation
        mutation_rate = 0.3
        random_ind = np.random.choice([i for i in range(population_size)], size=int(mutation_rate * population_size), replace=False)
        m = Mutation(mutation_type='swap')
        for i in random_ind:
            population[i].update_path(m.mutation(population[i].path))
        population.sort(key=operator.attrgetter('fitness'), reverse=False)
        print('best so far: %s' % population[0].fitness)
