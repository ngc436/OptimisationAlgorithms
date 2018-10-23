class Mutation:
    def __init__(self, mutation_type, **kwargs):
        self.mutation_type = mutation_type
        self.mutation_selector(**kwargs)

    def mutation_selector(self, **kwargs):
        if self.mutation_type == 'mutation_1':
            self.mutation_1()

    def mutation_1(self, **kwargs):
        raise NotImplementedError
