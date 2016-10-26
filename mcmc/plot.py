# subroutine to plot out the required graphs
# currently contains the function to plot specified graphs and most probable one
import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import operator
import ast


class PlotGraph:

    def __init__(self):
        pass

    # plot the graph specified in the bracket
    # save to output.png
    def plot_this_graph(self, k, pos, ind, mylist):
        # would like to share this property for all possible functions
        # may need optimization later
        plt.figure(figsize=(5, 5))
        fig = plt.figure()
        # draw graph with pos, actually not necessary
        # just in case I mess up the weights
        g = nx.empty_graph(k)
        list_edge = ast.literal_eval(mylist[ind-1])
        nx.draw_networkx(g, pos, edgelist=list_edge, node_size=20)
        fig.savefig('output.png')

    # a really ugly way to plot out the most probable graph
    # I first convert the list of edge list to string so that I can compare and count them
    # then I need restore the strings back to list and draw graph with 'edgelist' argument
    # require k, number of nodes
    #         pos, initial nodes positions
    # as I actually regenerate the graph from very beginning based on the sorted edge list
    # if only require an example of top 1%, current algorithm is ok
    # need improvement later
    def plot_most_probable(self, k, pos, edge_list, summary):
        # I/O
        histo = open('sorted_histogram', 'w')
        # again may require optimization
        plt.figure(figsize=(5, 5))
        fig = plt.figure()
        # dump out initial 1/5 of the list
        # the value is related to T, so may need to be modified once T is changed
        ind = len(edge_list)
        ind = ind//5
        edge_list = edge_list[ind:]
        # initialize a new dictionary
        hist = {}
        # begin count the histogram
        for elem in edge_list:
            if elem in hist:
                hist[elem] += 1
            else:
                hist[elem] = 1
        # sort the dictionary for output
        sorted_hist = sorted(hist.items(), key=operator.itemgetter(1), reverse=True)
        # write to file
        for i in range(len(sorted_hist)):
            print('{:6d}{}{}{:4d}'.format(i+1, '  ', sorted_hist[i][0], sorted_hist[i][1]), file=histo)
        histo.close()
        # convert the most probable string back to list
        list_edge = ast.literal_eval(sorted_hist[0][0])
        print('{}{}{}{}{}{}{}{}'.format('total number of graphs generated under assumed equilibrium  ', len(sorted_hist), "\n",
                                        'most probable graph structure (edges):  ', list_edge, "\n",
                                        'number of occurrence of this graph:  ', sorted_hist[0][1]), file=summary)
        # draw
        g = nx.empty_graph(k)
        nx.draw_networkx(g, pos, edgelist=list_edge, node_size=20)
        fig.savefig('top.png')
