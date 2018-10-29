from firefly_optimisation import FireflyOptimizer

f_alg = FireflyOptimizer(population_size=50, problem_dim=2, generations=100, beta_min=0.65, alpha=0.05)
f_alg.run_firefly()
