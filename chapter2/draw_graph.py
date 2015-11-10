#!/usr/bin/env python
import sys
import string

from GraphWorld import CircleLayout, GraphWorld
from graph import Vertex, Graph


order, degree = (int(i) for i in sys.argv[1:])

labels = string.ascii_lowercase
vertices = [Vertex(c) for c in labels[:order]]
graph = Graph(vertices)
graph.add_regular_edges(degree)

layout = CircleLayout(graph)

gw = GraphWorld()
gw.show_graph(graph, layout)
gw.mainloop()
