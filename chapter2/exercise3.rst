Chapter 2 Exercise 3
====================

Write a method named add_regular_edges that starts with an edgeless graph and
adds edges so that every vertex has the same degree. The degree of a node is
the number of edges it is connected to.

To create a regular graph with degree 2 you would do something like this::

    g = Graph([list of Vertices], [])
    g.add_regular_edges(2)

It is not always possible to create a regular graph with a given degree, so
you should figure out and document the preconditions for this method.

To test your code, you might want to create a file named GraphTest.py that
imports Graph.py and GraphWorld.py, then generates and displays the graphs you
want to test.
