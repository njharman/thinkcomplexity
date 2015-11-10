#!/usr/bin/env python
import sys
import string
from itertools import chain, product

from GraphWorld import CircleLayout, GraphWorld
from graph import Vertex, Graph, RandomGraph


labels = chain(string.ascii_lowercase, product(string.ascii_uppercase, range(1, 101)))


def draw(graph):
    layout = CircleLayout(graph)
    gw = GraphWorld()
    gw.show_graph(graph, layout)
    gw.mainloop()


def make_vertices(order):
    return [Vertex(c) for c in labels[:order]]


def regular(vertices, degree):
    degree = int(degree)
    graph = Graph(vertices)
    graph.add_regular_edges(degree)
    return graph


def random(vertices, p):
    p = float(p)
    graph = RandomGraph(vertices)
    graph.add_random_edges(p)
    return graph


if __name__ == '__main__':
    order = int(sys.argv[1])
    vertices = make_vertices(order)
    # graph = regular(vertices, sys.argv[2])
    graph = random(vertices, sys.argv[2])
    draw(graph)
