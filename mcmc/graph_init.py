# generate a empty graph with k nodes
# get position from pygraphviz module
# link all (0,k) edges to get a star graph

# import packages
import networkx as nx
import numpy as np
from networkx.drawing.nx_agraph import graphviz_layout
#import pygraphviz
import random
import math

class get_init():

    def __init__(self):
        pass

#   initialize a graph that all the other nodes
#   connect to node 0 and return the graph and position array
    def init_graph(self, k):
        G=nx.empty_graph(k)
        # get and store positions into array 'pos'
        pos = nx.spring_layout(G, dim=2)
        for i in range(1,k):
            G.add_edge(0, i)
        return G,pos

#   calculate the weight of all the possible edges and
#   store the values into a matrix for future use
    def calc_weight(self, pos, k):
        # initialize empty 2D array
        w = np.empty([k, k])
        # loop over all nodes
        for i in range(k):
            for j in range(k):
                square = 0
                for m in range(2):
                    square += (pos[i][m] - pos[j][m])**2
                w[i][j] = math.sqrt(square)
        return w



