import numpy as np


class Crossover:
    def __init__(self, crossover_type, **kwargs):
        self.crossover_type = crossover_type

    def crossover(self, parent_1, parent_2, **kwargs):
        if self.crossover_type == self.crossover_type:
            self.crossover_pmx(parent_1=parent_1, parent_2=parent_2)

    def crossover_pmx(self, **kwargs):
        parent_1 = kwargs.get('parent_1')
        parent_2 = kwargs.get('parent_2')
        points_num = len(parent_1)
        cut_ix = np.random.choice(points_num - 2, 2, replace=False)
        min_ix = np.min(cut_ix)
        max_ix = np.max(cut_ix)
