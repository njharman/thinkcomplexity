Chapter 3 Exercise 4
====================

My implementation of HashMap accesses the attributes of BetterMap directly,
which shows poor object-oriented design.

The special method __len__ is invoked by the built-in function len. Write
a __len__ method for BetterMap and use it in add.

Use a generator to write BetterMap.iteritems, and use it in resize.
