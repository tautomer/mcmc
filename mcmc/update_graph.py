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

    def change_edges(self, k, G, keep, etot):
        # switch used to control the loop
        trail = G.copy()
        switch = 1
        while (switch):
            if (trail.number_of_edges() == etot):
                break
            else:
                # get two different random integers within [0,k]
                lim = random.sample(range(0, k), 2)
                lim.sort()
                # if edge exists
                if (lim[0] in trail.neighbors(lim[1])):
                    # if edge cannot be deleted, cycle
                    if [lim[0],lim[1]] in keep:
                        continue
                    else:
                        # else remove the edge
                        trail.remove_edge(lim[0],lim[1])
                else:
                    # add edge (lim[0],lim[1])
                    trail.add_edge(lim[0],lim[1])
                # jump out of the loop
                switch = 0
        return trail














