from data_utils import *
import operator
from GA_tsp_optimisation import Selector, Crossover, Mutation
from vis import *
from data_utils import create_matrix
import random

coordinates = None
matrix = None


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
    for i in range(len(path) - 1):
        if i == (len(path) - 1):
            dist += matrix[path[0]][path[i]]
            break
        dist += matrix[path[i + 1]][path[i]]
    return dist


def _generate_population(num_of_cities, population_size):
    population = []
    for _ in range(population_size):
        path = np.random.permutation([i for i in range(num_of_cities)])
        population.append(Path(path))
        # draw_path(path, coordinates)
    return population


def ga_pipeline(mat=None, population_size=20, generations=200, best_perc=0.2,
                mutation_rate=0.2, mutation_intensity=0.3,
                verbose=1, coord=None, plot=0):
    num_of_cities = mat.shape[0]
    global matrix
    matrix = mat
    global coordinates
    coordinates = coord
    population = _generate_population(num_of_cities, population_size)
    s = Selector(selection_type='roulette')
    c = Crossover(crossover_type='ordered')
    m = Mutation(mutation_type='rsm')
    x, y = [], []
    for ii in range(generations):
        population.sort(key=operator.attrgetter('fitness'), reverse=False)
        new_generation = []
        for i in range(int(population_size * best_perc)):
            new_generation.append(population[i])
        pairs_generator = s.selection(population=population, best_perc=best_perc)
        for i, j in pairs_generator:
            child_1, child_2 = c.crossover(parent_1=i.path, parent_2=j.path)
            new_generation.append(Path(child_1))
            new_generation.append(Path(child_2))
        population = new_generation[:population_size]
        for i in range(1, len(population)):
            if random.random() < mutation_rate:
                population[i].update_path(m.mutation(population[i].path))
        population.sort(key=operator.attrgetter('fitness'), reverse=False)
        if verbose:
            print('========== generation %s ==========' % ii)
            print('best so far: %s\n' % population[0].fitness)
        x.append(ii)
        y.append(population[0].fitness)
        if plot:
            if ii % 500 == 0:
                draw_path(population[0].path, coordinates, ii)
    draw_convergence(x, y, 'ps = %s, bp = %s, mr = %s, mi = %s' % (
            round(population_size, 2), round(best_perc, 2), round(mutation_rate,2), round(mutation_intensity, 2)))
    return population[0].fitness
