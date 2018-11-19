import numpy as np
import random


class Mutation:
    def __init__(self, mutation_type, **kwargs):
        self.mutation_type = mutation_type

    def mutation(self, individ, **kwargs):
        if self.mutation_type == 'rsm':
            return self.rsm(individ=individ, **kwargs)
        if self.mutation_type == 'swap':
            return self.swap_mutation(individ=individ, **kwargs)

    def rsm(self, **kwargs):
        individ = kwargs.get('individ')
        print(individ)
        ix = np.random.choice(len(individ), 2, replace=False).tolist()
        sub = individ[min(ix), max(ix)]
        print(ix, sub)

    def swap_mutation(self, **kwargs):
        individ = kwargs.get('individ')
        mutation_intensity = kwargs.get('mutation_intensity')
        for _ in range(int(len(individ) * mutation_intensity)):
            if random.random() > 0.5:
                ix = np.random.choice(len(individ), 2, replace=False)
                tmp = individ[ix[0]]
                individ[ix[0]] = individ[ix[1]]
                individ[ix[1]] = tmp
        return individ


m = Mutation('rsm')
m.mutation(individ=[0, 1, 2, 3, 4, 5, 6, 7, 8])
