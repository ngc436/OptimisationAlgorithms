from data_utils import create_matrix, read_tsp_file
from GA_tsp_optimisation import ga_pipeline
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials

fname = 'xqf131.tsp'

matrix = create_matrix(fname)
coord = read_tsp_file(fname)


def ga_wrapper(params):
    population_size = int(params['population_size'])
    best_perc = params['best_perc']
    mutation_rate = params['mutation_rate']
    val = ga_pipeline(mat=matrix, population_size=population_size,
                      best_perc=best_perc, mutation_rate=mutation_rate, generations=500, verbose=0)
    print(params, val)
    return {'loss': val, 'status': STATUS_OK}


def hyperopt_optimization():
    trials = Trials()

    space = {
        'best_perc': hp.uniform('best_perc', 0.1, 0.8),
        'population_size': hp.quniform('population_size', 3, 100, 1),
        'mutation_rate': hp.uniform('mutation_rate', 0.1, 0.8)
    }

    best = fmin(
        ga_wrapper,
        space=space,
        algo=tpe.suggest,
        max_evals=100,
        trials=trials
    )

    return best


def run_tsp(population_size, best_perc, mutation_rate, genetations, coord):
    val = ga_pipeline(mat=matrix, population_size=population_size,
                      best_perc=best_perc, mutation_rate=mutation_rate,
                      generations=genetations, verbose=1, coord=coord)
    return val


def main():
    # print(hyperopt_optimization())
    print(
        run_tsp(mutation_rate=0.6281968256374211, best_perc=0.10407029186545108,
                population_size=92, genetations=10000, coord=coord))


if __name__ == '__main__':
    main()
