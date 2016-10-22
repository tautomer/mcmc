# -*- coding: utf-8 -*-
# The main program for Markov chain Monte Carlo simulation
# This program requires four initial parameters, k, r, T and nstep.
# where k is the number of nodes, r is the weight coefficient.
# T is time step, nsteps is total number of steps, i.e., graphs.
# They are specified at the beginning of the program.

# Begin importing packages
from graph_init import get_init
from update_graph import update_graph
from monte_carlo import monte_carlo
import networkx as nx
# Set parameters
k = 8
r = 1
T = 0.1
nsteps = 3

# calculate number of all possible edges
etot = k*(k-1)/2
# aliases
gi = get_init()
ug = update_graph()
mc = monte_carlo()
# Generate initial graph and get positions of all nodes
# G is the graph and pos is the matrix storing positions
G, pos = gi.init_graph(k)
# calculate weight
w = gi.calc_weight(pos,k)
# check spanning trees

graph = [None]*0
graph.append(G)
for i in range(1, nsteps):
    B, keep = ug.chk_spanning(graph[i-1])
    H = ug.change_edges(k, graph[i-1], keep, etot)
    graph.append(H)
    theta_i = mc.calc_theta(graph[i-1], w)
    nx.write_edgelist(G, 'test.edgelist', data=['weight'])

#rint(graph[0].edges())

