#!/usr/bin/env python
import sys
import string

from GraphWorld import CircleLayout, GraphWorld
from graph import Vertex, Graph, RandomGraph


def draw(graph):
    layout = CircleLayout(graph)
    gw = GraphWorld()
    gw.show_graph(graph, layout)
    gw.mainloop()


def regular(vertices):
    degree = int(sys.argv[2])
    graph = Graph(vertices)
    graph.add_regular_edges(degree)
    return graph


def random(vertices):
    p = float(sys.argv[2])
    graph = RandomGraph(vertices)
    graph.add_random_edges(p)
    return graph


labels = string.ascii_lowercase
order = int(sys.argv[1])
vertices = [Vertex(c) for c in labels[:order]]

# graph = regular(vertices)
graph = random(vertices)
draw(graph)
