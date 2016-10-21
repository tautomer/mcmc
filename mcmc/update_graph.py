# update the old graph to new one
# calculate probability and return to main program
import networkx as nx
import random

class update_graph():

    def __init__(self):
        pass

    def chk_spanning(self, G):
        # initialize counter
        B = 0
        # initialize a empty list to store necessary edegs
        keep = [None]*0
        # loop over all current edges
        for u,v in G.edges():
            G.remove_edge(u,v)
            if(nx.is_connected(G)):
                pass
            else:
                # update counter
                B += 1
                # update list
                keep.append([u,v])
            # restore edge
            G.add_edge(u,v)
        return B,keep

    def change_edges(self, k, G, keep):
        # switch used to control the loop
        switch = 1
        while (switch):
            # get two different random integers within [0,k]
            m,n = random.sample(range(0, k), 2)
            # generate the random number to control add or remove edges
            ctrl = random.randint(0,1)
            if (ctrl):
                # add edge (m,n)
                # if edge already exists, cycle
                if (m in G.neighbors(n)):
                    continue
                else:
                    # if not, add edge
                    G.add_edge(m,n)
            else:
                # delete edge (m,n)
                # if this edge cannot be cut, cycle
                if [m,n] in keep or [n,m] in keep :
                    continue
                else:
                    # if not, remove it
                    G.remove_edge(m,n)
            # jump out of the loop
            switch = 0
            return G














