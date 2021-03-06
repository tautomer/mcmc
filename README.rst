==================================
mcmc ---- Markov Chain Monte Carlo
==================================

.. image:: https://travis-ci.org/tautomer/mcmc.svg?branch=master
        :target: https://travis-ci.org/tautomer/mcmc

.. image:: https://readthedocs.org/projects/markov-chain/badge/?version=latest
        :target: http://markov-chain.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://coveralls.io/repos/github/tautomer/mcmc/badge.svg?branch=master
        :target: https://coveralls.io/github/tautomer/mcmc?branch=master


A small program for Markov chain Monte Carlo simulations.


Features
--------

Currently you can run the program from anywhere you like by typing 'python3 path_to_source_code_folder/mcmc.py'. Output
files will saved to the folder where you run the command.
There are four parameters for this program,

k ---------- the number of nodes

r ---------- the weight coefficient

T ---------- temperature

nsteps ----- number of total steps ( graphs ).

You can modify those parameters in mcmc/mcmc.py

* Note: The simulations is highly sensitive to temperature. High temperature leads to fast convergence, while less stable distribution, i.e., you will get more kinds of graphs. On the other hand, low temperature causes several times slower convergence and failing in ergodicity assumption.
* Ergodicity can be verified with smaller number of nodes, e.g., 5 or 6, and a reasonable number of steps.

The program will produce several output files.

The list of all edges will be written into 'edgelist'.

The file 'output' contains number of steps, average degree of node 0, average number of edges, and average max length of all shortest paths
from 0, respectively, and they are stored step by step to show the time evolution, which can also be used to check convergence.

The arbitrary graph needed to be drawn is named 'output.png', while most probable one is called 'top.png'. Note that I do not
really count whether it is top 1% or not. Instead, I simply draw the one with highest histogram. In general, this range is tighter
than 1%.

The sorted histograms are stored in 'sorted_histogram', where the columns are indices, edges and histograms, respectively.

Some summarized information is saved to 'summary' for your convenience.


* Free software: MIT license
* Documentation: latest_ 
.. _latest: http://markov-chain.readthedocs.io/en/latest/


Todo
----
* Some improvements on draw.py.


Credits
-------

This package was created with Cookiecutter_ and the audreyr/cookiecutter-pypackage_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _audreyr/cookiecutter-pypackage: https://github.com/audreyr/cookiecutter-pypackage

