import numpy as np


class Crossover:
    def __init__(self, crossover_type, **kwargs):
        self.crossover_type = crossover_type

    def crossover(self, parent_1, parent_2, **kwargs):
        if self.crossover_type == 'pmx':
            return self.crossover_pmx(parent_1=parent_1, parent_2=parent_2)
        if self.crossover_type == 'ordered':
            return self.ordered_crossover(parent_1=parent_1, parent_2=parent_2)

    def crossover_pmx(self, **kwargs):
        parent_1 = kwargs.get('parent_1')
        parent_2 = kwargs.get('parent_2')
        points_num = len(parent_1)
        cut_ix = np.random.choice(points_num - 2, 2, replace=False)
        min_ix = np.min(cut_ix)
        max_ix = np.max(cut_ix)

    def ordered_crossover(self, **kwargs):
        parent_1 = kwargs.get('parent_1')
        parent_2 = kwargs.get('parent_2')
        points_num = len(parent_1)
        cut_ix = np.random.choice(points_num - 2, 2, replace=False)
        min_ix = np.min(cut_ix)
        max_ix = np.max(cut_ix)
        print(min_ix, max_ix)
        offspring_1 = np.zeros(points_num)
        current_ix = 0
        set_1 = parent_1[min_ix:max_ix]
        print(set_1)
        for i, elem in enumerate(parent_2):
            if elem not in set_1:
                print(i, elem, current_ix)
                if current_ix != min_ix:
                    offspring_1[current_ix] = elem
                else:
                    current_ix = max_ix
                    offspring_1[current_ix] = elem
                current_ix += 1
        offspring_1[min_ix:max_ix] = set_1
        offspring_2 = np.zeros(points_num)
        current_ix = 0
        set_2 = parent_2[min_ix:max_ix]
        for i, elem in enumerate(parent_1):
            if elem not in set_2:
                print(i, elem, current_ix)
                if current_ix != min_ix:
                    offspring_2[current_ix] = elem
                else:
                    current_ix = max_ix
                    offspring_2[current_ix] = elem
                current_ix += 1
        offspring_2[min_ix:max_ix] = set_2
        return list(map(int, offspring_1)), list(map(int, offspring_2))
