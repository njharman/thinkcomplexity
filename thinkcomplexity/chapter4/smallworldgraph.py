'''Code exercise from Chapter 4 of "Think Complexity" by Allen B. Downey.
'''
from __future__ import print_function
from __future__ import absolute_import

import random

from ..chapter2.graph import *


class SmallWorldGraph(RandomGraph):
    def rewire(self, p):
        '''Randomly rewire graph using p as probability that edge is reconnected.

        Pick a vertex(v) and edge(e) to nearest clockwise neighbor(w).
        With probability p reconnect e with new w chosen uniformly from all vertices.
        Duplicate edges forbidden.
        Continue clockwise (to w) for one lap.
        Then repeat with with next nearest clockwise neighbor until all edges have
        been considered once.

        :param p: float 0 to 1.
        '''
        # How the fuck do you know what is clockwise?
        # Why not just iter0ate over all edges?
        p = self._normalize_p(p)
        vertices = self.vertices()
        for e in self.edges():
            if random.random() <= p:
                v, w = e
                while True:
                    new_w = random.choice(vertices)
                    if self.get_edge(v, new_w) is None:
                        break
                self.del_edge(e)
                self.add_edge(Edge(v, new_w))

    def clustering_coefficient(self):
        '''Calculate the fraction of all possible edges a vertex has, averaged
        over all vertices.
        '''
        most = self.order() - 1  # Vertex can have at most n-1 edges where n is number of vertices in graph.
        fractions = list()
        for v in self.vertices():
            fractions.append(len(self.out_edges(v)) / most)
        return sum(fractions) / self.order()
