from __future__ import print_function

from graph import Graph, RandomGraph, Vertex
import draw_graph as dg


def test():
    print('\nconnected', g.is_connected())


g = RandomGraph([Vertex(i) for i in range(20)])
g.add_random_edges(.17)
# g.add_regular_edges(2)


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", number=10, setup="from __main__ import test;"))
    dg.draw(g)
