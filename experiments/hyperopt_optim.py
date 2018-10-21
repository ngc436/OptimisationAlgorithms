# 200 dim optimization

from optimisation import FireflyOptimizer
from hyperopt import STATUS_OK, Trials, fmin, hp, tpe


def score(params):
    f_alg = FireflyOptimizer(**params)
    fitness, position = f_alg.run_firefly()
    return {'loss': -fitness, 'status': STATUS_OK}


def optimize():
    space = {
        'population_size': hp.quniform('population_size', 10, 200, 1),
        'gamma': hp.quniform('gamma', 0.5, 1, 0.05),
        'alpha': hp.quniform('alpha', 0, 1, 0.05),
        'beta_min': hp.quniform('beta_min', 0, 1, 0.05),
        # optimize for the below params
        'problem_dim': 200,
        'generations': 50
    }
    best = fmin(score, space, algo=tpe.suggest, max_evals=100)
    return best

best_hyperparams = optimize()
print(best_hyperparams)
