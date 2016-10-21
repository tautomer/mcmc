# subroutine to handle the core part for monte carlo simulation

# import packages
import networkx as nx

class monte_carlo():

    def __init__(self):
        pass

    def calc_theta(self, G, w):
        for u,v in G.edges():
            G.add_edge(u,v,weight=w[u][v])
        sum_all_weight = G.size(weight='weight')
        all_path_0 = nx.single_source_dijkstra_path_length(G,0)
        sum_length_0 = sum(all_path_0.values())
        theta = sum_all_weight + sum_length_0
        return theta

    def calc_prob(self, keep, k):
        prob = k*(k-1)/2 - len(keep)
        return prob

    def metripolis(self, ):
        pass


