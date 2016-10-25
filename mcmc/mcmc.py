# -*- coding: utf-8 -*-
# The main program for Markov chain Monte Carlo simulation
# This program requires four initial parameters, k, r, T and nstep.
# where k is the number of nodes, r is the weight coefficient.
# T is temperature, nsteps is total number of steps, i.e., graphs.
# They are specified at the beginning of the program.

# Begin importing packages
from mcmc.graph_init import GetInit
from mcmc.update_graph import UpdateGraph
from mcmc.monte_carlo import MonteCarlo
from mcmc.plot import PlotGraph
import sys
import os
dir_root = os.path.realpath(
               os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
if not dir_root in sys.path:
    sys.path.insert(0, dir_root)

# Set parameters
k = 8
r = 1
T = 300
nsteps = 3000


# calculate number of all possible edges
etot = k*(k-1)/2
# aliases of my own modules
gi = GetInit()
ug = UpdateGraph()
mc = MonteCarlo()
pg = PlotGraph()


# Generate initial graph and get positions of all nodes
# G is the initial graph and pos is the matrix storing positions
G, pos = gi.init_graph(k)
# calculate weights of all possible edges
w = gi.calc_weight(pos, k)
# initialize the list graph to store all the graphs
graph = [None]*0
# initialize the list to store all the edge list in the type of string
edge_list = [None]*0
# write initial graph into graph[0]
graph.append(G)
# write initial edge list into edge_list[0]
edge_list.append(str(G.edges()))
# get the the number of neighbors of node 0
neighbor_0 = len(graph[0].neighbors(0))
# get the number of edges in the whole graph
n_edge = graph[0].number_of_edges()
# check necessary edges of the zeroth graph
keep_i = ug.chk_bridges(graph[0])
# calculate the probability q(j|i) for the zeroth graph
prob_i = mc.calc_prob(keep_i, etot)
# calculate thetas for zeroth graphs
theta_i, max_i = mc.calc_theta(graph[0], w, r)
# sum the maximum length
sum_max_len = max_i
# I/O part
expectations = open('output', 'w')
edges = open('edgelist', 'w')
summary = open('summary', 'w')
# output information
print('{}{}'.format('total number of nodes:  ', k), file=summary)
print('{}{}'.format('nodes postions:  ', pos), file=summary)
print('{}'.format(graph[0].edges()), file=edges)
print('{}{}{}{}'.format('nsteps  ', 'degree_0  ', 'n_edges  ', 'max_len'), file=expectations)
# begin loop over all steps
for i in range(1, nsteps):
    # get the new graph candidate tmp
    tmp = ug.change_edges(k, graph[i-1], keep_i)
    # check necessary edges of the candidate
    keep_j = ug.chk_bridges(tmp)
    # calculate the probability q(i|j)
    prob_j = mc.calc_prob(keep_j, etot)
    # calculate theta and maximum path length for candidate
    theta_j, max_j = mc.calc_theta(tmp, w, r)
    # run Metropolis
    tmp, theta_i, prob_i, keep_i, max_i = mc.metropolis(theta_i, theta_j, prob_i, prob_j, T, graph[i-1], tmp, keep_i, keep_j, max_i, max_j)
    # write initial graph into graph[i]
    # original graphs can be throw away now
    graph.append(tmp)
    # write edge list into edge_list
    edge_list.append(str(tmp.edges()))
    # quantities required for output
    neighbor_0 += len(graph[i].neighbors(0))
    n_edge += graph[i].number_of_edges()
    sum_max_len += max_i
    # for checking propose
    # since the convergence is really fast, I did not truncate the data ( need correct this probably )
    # plot out the 'trajectory' is pretty cool
    print('{:6d}{:9.4f}{:9.4f}{:9.4f}'.format(i, neighbor_0/(i+1), n_edge/(i+1), sum_max_len/(i+1)), file=expectations)
    print('{}'.format(graph[i].edges()), file=edges)

# print out the expected numbers of edges connected to vertex 0 and edges in the entire graph
print('{}{}{}{}{}'.format('the expected number of edges connected to vertex 0:  ', neighbor_0/nsteps, "\n", 'the expected number of edges in the entire graph:  ', n_edge/nsteps), file=summary)

# demo of output, just plot the last graph in the list
pg.plot_this_graph(pos, graph[nsteps-1])
pg.plot_most_probable(k, pos, edge_list, summary)
# close files
expectations.close()
edges.close()
summary.close()
