# subroutine to plot out the required graphs
# currently only contain the function to plot specified graphs
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import networkx.drawing

class plot_graph():
    # would like to share this property for all possible functions
    # not sure if it's correct to use like this
    plt.figure(figsize=(5,5))

    def __init__(self):
        pass
    # plot the graph specified in the bracket
    def plot_this_graph(self, pos, G):
        nx.draw_networkx(G, pos, node_size=20)
        plt.show()
