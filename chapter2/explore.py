#!/usr/bin/env python
from __future__ import print_function

from graph import Graph, RandomGraph, Vertex
import draw_graph as dg


def test():
    print('connected', g.is_connected())


g = RandomGraph([Vertex(i) for i in range(80)])
g.add_random_edges(.1)
# g.add_regular_edges(2)


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", number=10, setup="from __main__ import test;"))
    dg.draw(g, 1000)
