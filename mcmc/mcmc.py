# -*- coding: utf-8 -*-
# The main program for Markov chain Monte Carlo simulation
# This program requires two initial parameters, k and r,
# where k is the number of nodes, r is the weight coefficient.
# They are specified at the beginning of the program.

# Begin importing packages
from graph_init import get_init
#import networkx as nx
# Set parameters
k = 8
r = 1

# Generate initial graph and get positions of all nodes
gi=get_init()
# G is the graph and pos is the matrix storing positions
G, pos = gi.init_graph(k)
# calculate weight
w = gi.calc_weight(pos,k)

print(w)

