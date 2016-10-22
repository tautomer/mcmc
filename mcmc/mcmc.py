# -*- coding: utf-8 -*-
# The main program for Markov chain Monte Carlo simulation
# This program requires four initial parameters, k, r, T and nstep.
# where k is the number of nodes, r is the weight coefficient.
# T is time step, nsteps is total number of steps, i.e., graphs.
# They are specified at the beginning of the program.

# Begin importing packages
from mcmc.graph_init import get_init
from mcmc.update_graph import update_graph
from mcmc.monte_carlo import monte_carlo
from mcmc.plot import plot_graph
import networkx as nx

# Set parameters
k = 8
r = 1
# this value is highly related to the value of theta
# need think if it's necessary to associate T with weight automatically
T = 80
nsteps = 10000

# calculate number of all possible edges
etot = k*(k-1)/2
# aliases of my own modules
gi = get_init()
ug = update_graph()
mc = monte_carlo()
pg = plot_graph()

# Generate initial graph and get positions of all nodes
# G is the initial graph and pos is the matrix storing positions
G, pos = gi.init_graph(k)

# calculate weights of all possible edges
w = gi.calc_weight(pos,k)

# initialize the list graph to store all the graphs
graph = [None]*0
# write initial graph into graph[0]
graph.append(G)

# begin loop over all steps
for i in range(1, nsteps):
    # check necessary edges of the (i-1)th graph
    # can be optimized later
    keep = ug.chk_spanning(graph[i-1])
    # calculate the probability q(j|i)
    prob_i = mc.calc_prob(keep, etot)
    # get the new graph candidate tmp
    tmp = ug.change_edges(k, graph[i-1], keep, etot)
    # check necessary edges of the candidate and overwrite the array keep
    keep = ug.chk_spanning(tmp)
    # calculate the probability q(i|j)
    prob_j = mc.calc_prob(keep, etot)
    # calculate thetas for both graphs
    theta_i = mc.calc_theta(graph[i-1], w, r)
    theta_j = mc.calc_theta(tmp, w, r)
    # run Metropolis and update graph list based on acceptance
    graph.append(mc.metropolis(theta_i, theta_j, prob_i, prob_j, T, graph[i-1], tmp))

# demo of output, just plot the last two graphs in the list
pg.plot_this_graph(pos, graph[nsteps-2])
pg.plot_this_graph(pos, graph[nsteps-1])

