import numpy as np


def read_tsp_file(fname):
    with open('data/%s' % fname) as f:
        while f.readline() != 'TYPE : TSP\n':
            pass
        points_count = int(f.readline().split(':')[1])
        print('Number of cities in the path:', points_count)
        while f.readline() != 'NODE_COORD_SECTION\n':
            pass
        coord = np.zeros(shape=(points_count, 2))
        for i in range(points_count):
            coord[i] = f.readline().split()[1:]
    return coord
