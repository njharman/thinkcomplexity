Chapter 3 Exercise 1
====================

Read the Wikipedia page on Big-Oh notation at
http://en.wikipedia.org/wiki/Big_O_notation and answer the following
questions:

What is the order of growth of n^3+n^2?
---------------------------------------
O(n^3), slower growing terms are ignored.

What about 1000000n^3+n^2?
---------------------------
O(n^3), constants are (largely) ignored.

What about n^3+1000000n^2?
---------------------------
O(n^3)

What is the order of growth of (n^2+n) * (n+1)?
--------------------------------------------------
Hmmm, is in n^3 cause n^2 * n? or n^2?

If f is in O(g), for some unspecified function g, what can we say about a f + b?
--------------------------------------------------------------------------------
wtf is b?  f+g O(f+g)

If f1 and f2 are in O(g), what can we say about f1 + f2?
--------------------------------------------------------
Beats me, O(g)?

If f1 is in O(g) and f2 is in O(h), what can we say about f1 + f2?
------------------------------------------------------------------
O(g+h)

If f1 is in O(g) and f2 is O(h), what can we say about f1 * f2?
---------------------------------------------------------------
O(gh)
