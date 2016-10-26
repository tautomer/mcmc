#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_mcmc
----------------------------------

Tests for `mcmc` module.
"""


import networkx as nx
import unittest
from mcmc.graph_init import GetInit
from mcmc.update_graph import UpdateGraph
from mcmc.monte_carlo import MonteCarlo
from mcmc.plot import PlotGraph

mc = MonteCarlo()
pg = PlotGraph()


class TestInit(unittest.TestCase):

    def setUp(self):
        self.init = GetInit()

#    def tearDown(self):
#        pass

#    def test_000_something(self):
#        pass

    def test_init_graph_fail_with_string_input(self):
        self.assertRaises(ValueError, self.init.init_graph, 1.2)

    def test_init_graph_success_with_string_input(self):
        g, test = self.init.init_graph(4)
        self.assertEqual(True, nx.is_connected(g))

    def test_calc_weight_return_correct_values(self):
        mydict = {0: [0, 3], 1: [4, 0]}
        w = self.init.calc_weight(mydict, 2)
        self.assertEqual(w[0][1], w[1][0])


class TestUpdate(unittest.TestCase):

    def setUp(self):
        self.up = UpdateGraph()
        self.init = GetInit()

    def test_chk_bridges_return_the_correct_value(self):
        g, temp = self.init.init_graph(4)
        mylist = self.up.chk_bridges(g)
        self.assertEqual(3, len(mylist))

    def test_update_graph_returns_different_graphs(self):
        g, temp = self.init.init_graph(4)
        keep = [[0,1], [0,2], [0,3]]
        test = self.up.change_edges(4, g, keep)
        self.assertEqual(False, nx.is_isomorphic(g, test))




