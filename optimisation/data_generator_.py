from numpy.random import random_sample


def generate_population(population_size, problem_dim, min_bound, max_bound):
    error = 1e-10
    data = (max_bound + error - min_bound) * random_sample((population_size, problem_dim)) + min_bound
    data[data > max_bound] = max_bound
    print(data)
    return data
