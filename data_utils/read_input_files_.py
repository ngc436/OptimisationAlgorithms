import numpy as np
import os
from scipy.spatial.distance import euclidean


def read_tsp_file(fname):
    with open(os.path.dirname(__file__) + '/data/%s' % fname) as f:
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


def create_matrix(fname):
    coord = read_tsp_file(fname)
    full_name = os.path.dirname(__file__) + '/data/%s_matrix.npy' % fname.split()[0]
    try:
        matrix = np.load(full_name)
    except:
        matrix = np.zeros((len(coord), len(coord)))
        for i in range(len(coord)):
            for j in range(len(coord)):
                matrix[i][j] = euclidean(coord[i], coord[j])
        np.save(full_name, matrix)
    return matrix
