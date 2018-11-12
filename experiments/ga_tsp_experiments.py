from data_utils import read_input_files_, read_tsp_file
from GA_tsp_optimisation import ga_pipeline
# TODO: move vis to ga_pipeline
from vis import *

fname = 'xqf131.tsp'
coord = read_tsp_file(fname)
plot_points(coord, 'Benchmark %s' % fname)
ga_pipeline(coord)
