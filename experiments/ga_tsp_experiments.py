from data_utils import read_input_files_, read_tsp_file, create_matrix
from GA_tsp_optimisation import ga_pipeline
# TODO: move vis to ga_pipeline
from vis import *

fname = 'xqf131.tsp'
coord = read_tsp_file(fname)
matrix = create_matrix(fname)
plot_points(coord, 'Benchmark %s' % fname)
ga_pipeline(mat=matrix)
