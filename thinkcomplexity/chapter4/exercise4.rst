Chapter 4 Exercise 4
====================
Create a file named SmallWorldGraph.py and define a class named
SmallWorldGraph that inherits from RandomGraph.

If you did Exercise 2.4 you can use your own RandomGraph.py; otherwise you can
download mine from thinkcomplex.com/RandomGraph.py.

  1. Write a method called rewire that takes a probability p as a parameter
     and, starting with a regular graph, rewires the graph using Watts and
     Strogatz’s algorithm.
  2. Write a method called clustering_coefficient that computes and returns
     the clustering coefficient as defined in the paper.
  3. Make a graph that replicates the line marked C(p)/C(0) in Figure 2 of the
     paper. In other words, confirm that the clustering coefficient drops off
     slowly for small values of p.
