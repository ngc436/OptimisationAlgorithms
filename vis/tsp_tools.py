import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import re
import os


def plot_points(coords, title='Benchmark'):
    plt.scatter(coords[:, 0], coords[:, 1], s=8, marker=".")
    plt.title(title)
    plt.show()
    plt.savefig('%s\\%s\\%s' % (os.path.dirname(__file__), 'Figures', re.sub(r'(\.[A-Za-z0-9]+)| ', "_", title)))

def draw_path(path, coords):
    fig, ax = plt.subplots()
    plot_coords = np.array([[coords[i][0],coords[i][1]] for i in path])
    # ax.set_xlim(np.min(plot_coords[]), np.max(x_coord))
    # ax.set_ylim(np.min(y_coord), np.max(y_coord))
    #
    # line_segments = LineCollection([np.column_stack([x_coord, y_coord]) for y in ys],
    #                            linewidths=(0.5, 1, 1.5, 2),
    #                            linestyles='solid')
