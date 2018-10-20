from optimization import FireflyOptimizer

f_alg = FireflyOptimizer(population_size=40, problem_dim=200, generations=10000)
f_alg.run_firefly()
