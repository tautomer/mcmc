# update the old graph to new one
# calculate probability and return to main program
import networkx as nx

class update_graph():

    def __init__(self):
        pass

    def chk_spanning(self, G):
        # initialize counter
        B = 0
        # loop over all current edges
        for u,v in G.edges():
            G.remove_edge(u,v)
            if(nx.is_connected(G)):
                G.add_edge(u,v)
            else:
                B += 1







