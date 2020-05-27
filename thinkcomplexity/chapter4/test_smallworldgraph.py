from __future__ import absolute_import

import pytest

from thinkcomplexity.chapter2.graph import *
from thinkcomplexity.chapter4.smallworldgraph import make_vertices, SmallWorldGraph


class TestSmallWorldGraph(object):
    def test_rewire(self):
        vertices = make_vertices(10)
        g = SmallWorldGraph(vertices)
        g.add_regular_edges(2)
        g.rewire(1)

    def test_clustering_coefficient(self):
        vertices = make_vertices(10)
        g = SmallWorldGraph(vertices)
        assert 0 == g.clustering_coefficient()
        g.add_all_edges()
        assert 1 == g.clustering_coefficient()
