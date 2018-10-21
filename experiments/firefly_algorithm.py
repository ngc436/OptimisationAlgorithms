from optimization import FireflyOptimizer

f_alg = FireflyOptimizer(population_size=50, problem_dim=200, generations=10000, beta_min=0.65, alpha=0.05)
f_alg.run_firefly()
