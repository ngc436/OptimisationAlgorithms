import numpy as np


class Mutation:
    def __init__(self, mutation_type, **kwargs):
        self.mutation_type = mutation_type

    def mutation(self, individ, **kwargs):
        if self.mutation_type == 'mutation_1':
            return self.mutation_1()
        if self.mutation_type == 'swap':
            return self.swap_mutation(individ=individ)

    def mutation_1(self, **kwargs):
        raise NotImplementedError

    def swap_mutation(self, **kwargs):
        individ = kwargs.get('individ')
        ix = np.random.choice(len(individ), 2, replace=False)
        tmp = individ[ix[0]]
        individ[ix[0]] = individ[ix[1]]
        individ[ix[1]] = tmp
        return individ
