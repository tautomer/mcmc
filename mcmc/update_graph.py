# update the old graph to new one
# calculate probability and return to main program

# begin import packages
import networkx as nx
import random


class UpdateGraph:

    def __init__(self):
        pass

    # check necessary edges for the target graph, G
    # though called spanning, this isn't truly checking spanning trees
    # just loop over and all edges, delete and check connectedness
    def chk_spanning(self, G):
        # initialize a empty list to store necessary edges
        keep = [None]*0
        # loop over all current edges
        for u, v in G.edges():
            # remove this edge
            G.remove_edge(u, v)
            # check connectedness
            if nx.is_connected(G):
                # if connected, pass
                pass
            else:
                # if not, append list
                keep.append([u,v])
            # restore the deleted edge
            G.add_edge(u, v)
        # return the list for necessary edges
        return keep

    # the function to update the graph
    # get a set of 2 random integer within [0,k]
    # if corresponding edge exists and isn't necessary, delete
    # otherwise, cycle to get a new set
    # if edge doesn't exist, just add the edge
    def change_edges(self, k, g, keep):
        # deep copy to get the new graph
        # all operations are towards the new one
        trail = g.copy()
        # switch used to control the loop
        switch = 1
        # a while loop, controlled by switch
        while switch:
            # get two different random integers within [0,k]
            lim = random.sample(range(0, k), 2)
            # sort the array to avoid troubles
            lim.sort()
            # if edge exists
            if lim[0] in trail.neighbors(lim[1]):
                # if edge cannot be deleted, cycle
                if [lim[0],lim[1]] in keep:
                    continue
                else:
                    # else remove the edge
                    trail.remove_edge(lim[0], lim[1])
            else:
                # add edge (lim[0],lim[1])
                trail.add_edge(lim[0], lim[1])
            # jump out of the loop
            switch = 0
        return trail
