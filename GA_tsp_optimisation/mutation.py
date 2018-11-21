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
        ix_len = 0
        while ix_len < 1:
            ix = np.random.choice(len(individ), 2, replace=False)
            ix_len = len(ix)
        sub = individ[min(ix): max(ix)]
        sub = sub[::-1]
        individ[min(ix): max(ix)] = sub
        return individ

    # def

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
