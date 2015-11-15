Chapter 3 Exercise 5
====================

A drawbacks of hashtables is that the elements have to be hashable, which
usually means they have to be immutable. That's why, in Python, you can use
tuples but not lists as keys in a dictionary. An alternative is to use
a tree-based map.

Write an implementation of the map interface called TreeMap that uses
a red-black tree to perform add and get in log time.
