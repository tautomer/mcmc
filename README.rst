===============================
mcmc ---- Markov Chain Monte Carlo
===============================
.. role:: red

.. image:: https://travis-ci.org/tautomer/mcmc.svg?branch=master
        :target: https://travis-ci.org/tautomer/mcmc

.. image:: https://readthedocs.org/projects/markov-chain/badge/?version=latest
        :target: http://markov-chain.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://coveralls.io/repos/github/tautomer/mcmc/badge.svg?branch=master
        :target: https://coveralls.io/github/tautomer/mcmc?branch=master



A small program for Markov chain Monte Carlo simulations.

Currently you can run the program under the root directory by 'python3 mcmc/mcmc.py'. 
There are four parameters for this program,

k ---------- the number of nodes

r ---------- the weight coefficient

T ---------- temperature

nsteps ----- number of total steps ( graphs ).

You can modify those parameters in mcmc/mcmc.py

* Note: The simulations is highly sensitive to temperature. High temperature leads to fast convergence, while less stable distribution, i.e., you will get more kinds of graphs. On the other hand, low temperature causes several times slower convergence and failing in elasticity assumption.

The program will produce several output files.

The list of all edges will be written into ':red:`edgelist`'.

The file ':red`output`' contains :red:`number of steps`, :red:`average degree of node 0`, :red:`average number of edges`, :red:`and average max length of all shortest paths
from 0`, respectively, and they are stored step by step to show the time evolution, which can also be used to check convergence.

The :red:`arbitrary` graph needed to be plotted is named ':red:`output.png`', while :red:`most probable` one is called ':red:`top.png`'. Note that :red:`I do not
really count whether it is top 1% or not. Instead, I simply plot the one with highest histogram. In general, this range is tighter
than 1%`.

The sorted histograms are stored in ':red:`sorted_histogram`', where the first column is edges and the second one is histograms.

Some summarized information is saved to ':red:`summary`' for your convenience.


* Free software: MIT license
* Documentation: https://mcmc.readthedocs.io.


Features
--------

Print out the final graph to the figure called output.png


Todo
--------
* Some improvements on plot.py.


Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

