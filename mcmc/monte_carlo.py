# subroutine to handle the core part for monte carlo simulation

# import packages
import networkx as nx
import math
import random

class monte_carlo():

    def __init__(self):
        pass

    # calculate theta for target graph
    def calc_theta(self, G, w, r):
        # retrieve weights from the array w
        # assign to sll connected edegs
        for u,v in G.edges():
            G.add_edge(u,v,weight=w[u][v])
        # use size function to get the sum of all weight
        sum_all_weight = G.size(weight='weight')
        # get all shortest path from node 0 and write to a dictionary
        all_path_0 = nx.single_source_dijkstra_path_length(G,0)
        # sum all length
        sum_length_0 = sum(all_path_0.values())
        # get theta
        theta = r*sum_all_weight + sum_length_0
        return theta

    # calculate the probability q(j|i)
    def calc_prob(self, keep, etot):
        prob = etot - len(keep)
        return prob

    # run Metropolis Monte Carlo
    # G_i is the old graph and G_j is the proposed new graph
    def metropolis(self, theta_i, theta_j, prob_i, prob_j, T, G_i, G_j):
        # the ratio of Pi_j and Pi_i
        temp = math.exp(-(theta_j - theta_i)/T)
        # the ratio of p_j and p_i
        temp1 = prob_j/prob_i
        # the value used to compare with 1
        temp2 = temp*temp1
        # get minimum
        aij = min(temp2, 1)
        # generate a random number for acceptance
        ran = random.uniform(0, 1)
        # if minimum is larger than random, accept the move
        if aij >= ran:
            pass
        else:
            # else, deep copy G_i to G_j, i.e., repeat
            G_j = G_i.copy()
        return G_j



