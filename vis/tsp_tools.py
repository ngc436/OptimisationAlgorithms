import matplotlib.pyplot as plt
import re
import os


def plot_points(coords, title='Benchmark'):
    plt.scatter(coords[:, 0], coords[:, 1], s=8, marker=".")
    plt.title(title)
    plt.show()
    plt.savefig('%s\\%s\\%s' % (os.path.dirname(__file__), 'Figures', re.sub(r'(\.[A-Za-z0-9]+)| ', "_", title)))


def draw_path(path, coords, iteration):
    for i in range(len(path) - 1):
        x = [coords[path[i]][0], coords[path[i + 1]][0]]
        y = [coords[path[i]][1], coords[path[i + 1]][1]]
        plt.plot(x, y, marker='o', markersize=2)
    plt.plot([coords[path[len(path)-1]][0], coords[path[0]][0]], [coords[path[len(path)-1]][1], coords[path[0]][1]], marker='o', markersize=2)
    plt.title('Mininmal path on %s iteration' % iteration)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def draw_convergence(x_list, y_list, params):
    plt.plot(x_list, y_list)
    plt.xlabel('Iteration')
    plt.ylabel('Minimal distance')
    plt.title('GA convergence %s'%params)
    plt.show()
