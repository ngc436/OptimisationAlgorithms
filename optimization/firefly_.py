class FireflyOptimizer:

    def __init__(self, **kwargs):
        self.population_size = kwargs.get('population_size',10)
        self.problem_dim = kwargs.get('problem_dim', 2)
        self.min_bound = kwargs.get('min_bound', -1)
        self.max_bound = kwargs.get('max_bound', 1)


    def start_algorithm(self, verbose=1):

