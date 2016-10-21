# -*- coding: utf-8 -*-
# The main program for Markov chain Monte Carlo simulation
# This program requires four initial parameters, k, r, T and nstep.
# where k is the number of nodes, r is the weight coefficient.
# T is time step, nsteps is total number of steps, i.e., graphs.
# They are specified at the beginning of the program.

# Begin importing packages
from graph_init import get_init
from update_graph import update_graph
import networkx as nx
# Set parameters
k = 8
r = 1
T = 0.1
nsteps = 10000

# aliases
gi = get_init()
ug = update_graph()
# Generate initial graph and get positions of all nodes
# G is the graph and pos is the matrix storing positions
G, pos = gi.init_graph(k)
# calculate weight
w = gi.calc_weight(pos,k)
# check spanning trees
B, keep = ug.chk_spanning(G)
G_de = G.copy()
G_de.add_edge(1,2)
print(G_de.edges(),G.edges())

