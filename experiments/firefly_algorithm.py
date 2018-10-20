from optimization import FireflyOptimizer
import hyperopt

f_alg = FireflyOptimizer(population_size=10, problem_dim=2, generations=10000)
f_alg.run_firefly()