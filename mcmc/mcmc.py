# -*- coding: utf-8 -*-
# The main program for Markov chain Monte Carlo simulation
# This program requires four initial parameters, k, r, T and nsteps.
# where k is the number of nodes, r is the weight coefficient.
# T is temperature, nsteps is total number of steps, i.e., graphs.
# They are specified at the beginning of the program.

# solve path problem
import sys
import os
# get source file directory so that the program can be executable from anywhere
dir_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))
sys.path.append(dir_root)
# Begin importing packages
from graph_init import GetInit
from update_graph import UpdateGraph
from monte_carlo import MonteCarlo
from draw import DrawGraph

# Set parameters
k = 8
r = 1
T = 300
nsteps = 300

# calculate number of all possible edges
etot = k*(k-1)/2
# aliases of my own modules
gi = GetInit()
ug = UpdateGraph()
mc = MonteCarlo()
pg = DrawGraph()


# Generate initial graph and all the inital properties needed for future use
# tmp is the initial graph and pos is the matrix storing positions
# and later 'tmp' will also be the name of all current graphs
tmp, pos = gi.init_graph(k)
# calculate weights of all possible edges
w = gi.calc_weight(pos, k)
# initialize the list to store all the edge list in the type of string
edge_list = [None]*0
# write initial edge list into edge_list[0] as a string
edge_list.append(str(tmp.edges()))
# get the the number of neighbors of node 0
neighbor_0 = len(tmp.neighbors(0))
# get the number of edges in the whole graph
n_edge = tmp.number_of_edges()
# check necessary edges of the zeroth graph
keep_i = ug.chk_bridges(tmp)
# calculate the inverse of probability q(j|i) for the zeroth graph
prob_i = mc.calc_prob(keep_i, etot)
# calculate thetas for zeroth graphs
theta_i, max_i = mc.calc_theta(tmp, w, r)
# sum the maximum length
sum_max_len = max_i

# I/O part
expectations = open('output', 'w')
edges = open('edgelist', 'w')
summary = open('summary', 'w')
# output information
print('{}{}'.format('total number of nodes:  ', k), file=summary)
print('{}{}'.format('nodes positions:  ', pos), file=summary)
print('{}'.format(tmp.edges()), file=edges)
print('{}{}{}{}{:6d}{:9.4f}{:9.4f}{:9.4f}'.format('nsteps  ', 'degree_0  ', 'n_edges  ', 'max_len',
                                                  1, neighbor_0, n_edge, sum_max_len), file=expectations)
# begin loop over all steps
for i in range(1, nsteps):
    # get the new graph candidate tmp_new
    tmp_new = ug.change_edges(k, tmp, keep_i)
    # check necessary edges of the candidate
    keep_j = ug.chk_bridges(tmp_new)
    # calculate the inverse of the probability q(i|j)
    prob_j = mc.calc_prob(keep_j, etot)
    # calculate theta and maximum path length for candidate
    theta_j, max_j = mc.calc_theta(tmp_new, w, r)
    # run Metropolis
    tmp, theta_i, prob_i, keep_i, max_i = mc.metropolis(theta_i, theta_j, prob_i, prob_j,
                                                        T, tmp, tmp_new, keep_i, keep_j, max_i, max_j)
    # write edge list into edge_list
    edge_list.append(str(tmp.edges()))
    # quantities required for output
    neighbor_0 += len(tmp.neighbors(0))
    n_edge += tmp.number_of_edges()
    sum_max_len += max_i
    # for checking propose
    # drawing of the 'trajectory' can be pretty cool
    print('{:6d}{:9.4f}{:9.4f}{:9.4f}'.format(i+1, neighbor_0/(i+1), n_edge/(i+1), sum_max_len/(i+1)), file=expectations)
    print('{}'.format(tmp.edges()), file=edges)

# print out the expected numbers of edges connected to vertex 0 and edges in the entire graph
print('{}{}{}{}{}'.format('the expected number of edges connected to vertex 0:  ', neighbor_0/nsteps, "\n",
                          'the expected number of edges in the entire graph:  ', n_edge/nsteps), file=summary)

# demo of output, just draw the last graph in the list
# nth graph needed
nth = nsteps
pg.draw_this_graph(k, pos, nth, edge_list)
# output sorted histogram and draw the most probable graph
# since the data will be truncated adn over-written for counting histogram under equilibrium
# it's recommended to draw the arbitrary one first
pg.draw_most_probable(k, pos, edge_list, summary)

# close files
expectations.close()
edges.close()
summary.close()
