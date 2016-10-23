===============================
mcmc
===============================


.. image:: https://travis-ci.org/tautomer/mcmc.svg?branch=dev
    :target: https://travis-ci.org/tautomer/mcmc

.. image:: https://readthedocs.org/projects/markov-chain/badge/?version=latest
        :target: http://markov-chain.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://coveralls.io/repos/github/tautomer/mcmc/badge.svg?branch=dev
     :target: https://coveralls.io/github/tautomer/mcmc?branch=dev



A small program for Markov chain Monte Carlo simulations.

Currently you can run the program under the root directory by 'python3 mcmc/mcmc.py'. 
There are four parameters for this program,
k ---------- the number of nodes
r ---------- the weight coefficient
T ---------- time step
nsteps ----- number of total steps ( graphs ).
You can modify those parameters in mcmc/mcmc.py


* Free software: MIT license
* Documentation: https://mcmc.readthedocs.io.


Features
--------

Print out the final graph to the figure called output.png


Todo
--------
* Move the main program, mcmc.py, to the root directory and hold the coverage test.
* Fulfill all the necessary functions.

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

