thinkcomplexity
===============

Exercises and explorations from the book Think Complexity http://www.greenteapress.com/compmod/

Goals
-----
  #. Explore tox usage.
  #. Python 2.7, 3.4, 3.5 compatibility.
  #. Clean Architecture (I suspect the exercise structure will prevent this).


Thoughts
--------

Chapter 2 Graphs
~~~~~~~~~~~~~~~~

Kind of crappy Graph classes...

Exercise 3, add_regular_edges: First exercise that required some thought.
After several false starts, I had to google solution.

Exercise 4, Not using binomial distribution. Not even sure how to.

Exercise 5, is_connected: Not fast on maximally connected graphs (degree n-1).
Shouldn't algo only visit each node once? Hmmm, was significantly faster moving
mark node to add neighbors to queue loop. Prior to that duplicate nodes would
be added to queue.

This led me to look at speed of add_all_edges, On^2? Not very fast. But, maybe
best possible?


Chapter 3 Analysis of Algorithms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Used bisect module and then wrote my own bisection2 in sort.py

Recently watched this lecture https://www.youtube.com/watch?v=fYlnfvKVDoM "All
Your Ducks In A Row: Data Structures in the Standard Library and Beyond"
(PyCon US) by Brandon Rhodes. An excellent adjunct to this chapter.

Didn't write unittests for any of mymap.py, yet (It's sort of throw away cause
dict exists).
