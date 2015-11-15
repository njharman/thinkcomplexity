Chapter 3 Exercise 2
====================
Read the Wikipedia page on sorting algorithms at
http://en.wikipedia.org/wiki/Sorting_algorithm and answer the following
questions:

What is a "comparison sort?"
----------------------------
Sorting algo that processes elements through single comparison operation.
Operator follow these two rules.

  #. if a<=b and b<=c then a<=c (transitivity)
  #. for all a and b, either a<=b or b<=a (trichotomy)


What is the best worst-case order of growth for a comparison sort?
------------------------------------------------------------------
nlogn


What is the best worst-case order of growth for any sort algorithm?
-------------------------------------------------------------------
n^2  Cause this is comparing every item to every other item.


What is the order of growth of bubble sort?
-------------------------------------------
n^2


What is the order of growth of radix sort?
------------------------------------------
n(k/d) keys of size k, digit size d. An integer (non comparison sort)


What preconditions do we need to use it?
----------------------------------------
It works on "numbers" only, keys or values.


What is a stable sort and why might it matter in practice?
----------------------------------------------------------

Order of otherwise == items is retained. Stable sorts are idempotent.  It
allows multi-pass sorting (sort by color, then size).


What is the worst sorting algorithm (that has a name)?
------------------------------------------------------
Selection Sort. n^2 best case and not stable. Although it doesn't use any more memory.


What sort algorithm does the C library use?
-------------------------------------------
Quick Sort

What sort algorithm does Python use?
------------------------------------
Tim Sort

Are these algorithms stable?
----------------------------
yes

Many of the non-comparison sorts are linear, so why does does Python use an O(n logn) comparison sort?
------------------------------------------------------------------------------------------------------
So it can sort any type of types.
