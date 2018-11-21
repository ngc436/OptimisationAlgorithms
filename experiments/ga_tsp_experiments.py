from data_utils import create_matrix, read_tsp_file
from GA_tsp_optimisation import ga_pipeline
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials

fname = 'xqf131.tsp'

matrix = create_matrix(fname)
coord = read_tsp_file(fname)

# 564

def ga_wrapper(params):
    population_size = int(params['population_size'])
    best_perc = params['best_perc']
    mutation_rate = params['mutation_rate']
    val = ga_pipeline(mat=matrix, population_size=population_size,
                      best_perc=best_perc, mutation_rate=mutation_rate,
                      generations=20000, verbose=0, plot=0)
    print(params, val)
    return {'loss': val, 'status': STATUS_OK}


def hyperopt_optimization():
    trials = Trials()

    space = {
        'best_perc': hp.uniform('best_perc', 0.1, 0.9),
        'population_size': hp.quniform('population_size', 20, 50, 1),
        'mutation_rate': hp.uniform('mutation_rate', 0.1, 0.8)
    }

    best = fmin(
        ga_wrapper,
        space=space,
        algo=tpe.suggest,
        max_evals=50,
        trials=trials
    )

    return best


def run_tsp(population_size, best_perc, mutation_probability, generations, coord):
    val = ga_pipeline(mat=matrix, population_size=population_size,
                      best_perc=best_perc, mutation_probability=mutation_probability,
                      generations=generations, verbose=1, coord=coord, plot=1)
    return val


def main():
    # print(hyperopt_optimization())
    print(
        run_tsp(mutation_probability=0.4, best_perc=0.3,
                population_size=40, generations=5000, coord=coord))


if __name__ == '__main__':
    main()
