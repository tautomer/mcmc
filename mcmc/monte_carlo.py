# subroutine to handle the core part for monte carlo simulation

# import packages
import networkx as nx
import math
import random


class MonteCarlo():

    def __init__(self):
        pass

    # calculate theta for target graph
    def calc_theta(self, g, w, r):
        # retrieve weights from the array w
        # assign to sll connected edegs
        for u, v in g.edges():
            g.add_edge(u, v, weight=w[u][v])
        # use size function to get the sum of all weight
        sum_all_weight = g.size(weight='weight')
        # get all shortest path from node 0 and write to a dictionary
        all_path_0 = nx.single_source_dijkstra_path_length(g, 0)
        # sum all length
        sum_length_0 = sum(all_path_0.values())
        #  maximum distance of the shortest path that connects vertex 0
        max_len = max(all_path_0.values())
        # get theta
        theta = r*sum_all_weight + sum_length_0
        return theta, max_len

    # calculate the probability q(j|i)
    def calc_prob(self, keep, etot):
        prob = etot - len(keep)
        return prob

    # run Metropolis Monte Carlo
    # G_i is the old graph and G_j is the proposed new graph
    def metropolis(self, theta_i, theta_j, prob_i, prob_j, t, g_i, g_j, keep_i, keep_j, max_i, max_j):
        # the ratio of Pi_j and Pi_i
        temp = math.exp(-(theta_j - theta_i)/t)
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
            theta_i = theta_j
            prob_i = prob_j
            keep_i = keep_j
            max_i = max_j
        else:
            # else, deep copy G_i to G_j, i.e., repeat
            g_j = g_i.copy()
        return g_j, theta_i, prob_i, keep_i, max_i



