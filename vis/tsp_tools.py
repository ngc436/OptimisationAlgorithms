import numpy as np
import matplotlib.pyplot as plt
import re
import os


def plot_points(coords, title='Benchmark'):
    plt.scatter(coords[:, 0], coords[:, 1], s=8, marker=".")
    plt.title(title)
    plt.show()
    plt.savefig('%s\\%s\\%s' % (os.path.dirname(__file__), 'Figures', re.sub(r'(\.[A-Za-z0-9]+)| ', "_", title)))

def draw_path():
    raise NotImplementedError
