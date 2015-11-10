from __future__ import absolute_import

import pytest

from .graph import Vertex, Edge, Graph, GraphException


v = Vertex('v')
w = Vertex('w')
x = Vertex('x')
vw = Edge(v, w)
wv = Edge(w, v)
vx = Edge(v, x)
wx = Edge(w, x)


class TestVertex:
    def test_Vertex_str(self):
        assert str(Vertex()) == "Vertex('')"
        assert str(Vertex('foo')) == "Vertex('foo')"

    def test_Vertex_repr(self):
        assert repr(Vertex()) == "Vertex('')"
        assert repr(Vertex('foo')) == "Vertex('foo')"

    def test_Vertex_equality(self):
        # All Vertices are unique.
        assert Vertex() != Vertex()
        assert Vertex('v') != Vertex('v')

    def test_Vertex_sortable(self):
        assert [v, w, x] == sorted([x, v, w])

    def test_Vertex_hashable(self):
        assert dict(v=None)


class TestEdge:
    def test_Edge(self):
        assert str(Edge(v, w)) == "Edge(Vertex('v'), Vertex('w'))"
        assert repr(Edge(v, w)) == "Edge(Vertex('v'), Vertex('w'))"

    def test_Edge_equality(self):
        assert Edge(v, w) != Edge(v, x)
        assert Edge(v, w) == Edge(w, v)

    def test_Edge_sortable(self):
        assert [vw, vx] == sorted([vx, vw])


class TestGraph:
    def test_Graph_str(self):
        assert str(Graph()) == "Graph({})"

    def test_Graph_repr(self):
        assert repr(Graph()) == "Graph({})"

    def test_add_all_edges_empty(self):
        g = Graph()
        g.add_all_edges()
        assert g.vertices() == []
        assert g.edges() == []

    def test_add_all_edges(self):
        g = Graph([v, x, w])
        g.add_all_edges()
        assert sorted(g.vertices()) == sorted([v, x, w])
        assert len(g.edges()) == 3

    def test_add_regular_edges_negative(self):
        g = Graph()
        with pytest.raises(ValueError):
            g.add_regular_edges(-1)

    def test_add_regular_edges_invalid(self):
        g = Graph([v, w, x])
        # degree > vertexcount-1
        with pytest.raises(GraphException):
            g.add_regular_edges(3)
        # degree * vertexcount not even
        with pytest.raises(GraphException):
            g.add_regular_edges(1)

    def test_add_regular_edges_0(self):
        g = Graph()
        g.add_regular_edges(0)
        assert g.vertices() == []
        assert g.edges() == []
        g = Graph([v, w, x])
        g.add_regular_edges(0)
        assert sorted(g.vertices()) == sorted([v, x, w])
        assert g.edges() == []

    def test_add_regular_edges_1(self):
        g = Graph()
        g.add_regular_edges(0)
        assert g.vertices() == []
        assert g.edges() == []
        g = Graph([v, w, x])
        g.add_regular_edges(0)
        assert sorted(g.vertices()) == sorted([v, x, w])
        assert g.edges() == []

    def test_add_regular_edges_n(self):
        '''Degree * order(vertexcount) must be even.'''
        g = Graph([v, w, x])
        g.add_regular_edges(2)
        assert set(g.edges()) == set([vw, vx, wx])

    def test_get_edge_bad_input(self):
        g = Graph()
        assert g.get_edge(None, None) is None
        assert g.get_edge(None, v) is None
        assert g.get_edge(v, None) is None
        assert g.get_edge(v, 'fs') is None
        assert g.get_edge(v, 3) is None

    def test_get_edge_false(self):
        g = Graph()
        assert None is g.get_edge(v, v)
        assert None is g.get_edge(w, w)
        assert None is g.get_edge(v, w)
        assert None is g.get_edge(w, v)
        g = Graph([v, w])
        assert None is g.get_edge(v, v)
        assert None is g.get_edge(w, w)
        assert None is g.get_edge(v, w)
        assert None is g.get_edge(w, v)
        g = Graph([v, w, x], [vx, ])
        assert None is g.get_edge(v, v)
        assert None is g.get_edge(w, w)
        assert None is g.get_edge(v, w)
        assert None is g.get_edge(w, v)

    def test_get_edge_true(self):
        g = Graph([v, w], [vw, ])
        assert vw == g.get_edge(v, w)
        assert vw == g.get_edge(w, v)

    def test_vertices_empty(self):
        assert Graph().vertices() == []

    def test_vertices(self):
        g = Graph([v, w], [vw, ])
        assert sorted(g.vertices()) == sorted([v, w])

    def test_edges_empty(self):
        assert Graph().edges() == []

    def test_edges(self):
        g = Graph([v, w], [vw, ])
        assert g.edges() == [vw, ]
        g = Graph([v, w, x], [vw, vx])
        assert set(g.edges()) == set([vx, vw])

    def test_out_vertices_none(self):
        g = Graph()
        assert [] == g.out_vertices(v)

    def test_out_vertices(self):
        g = Graph([v, w, x], [vw, vx])
        assert sorted(g.out_vertices(v)) == sorted([w, x])
        assert g.out_vertices(w) == [v, ]
        assert g.out_vertices(x) == [v, ]

    def test_out_edges_none(self):
        g = Graph()
        assert [] == g.out_edges(v)

    def test_out_edges(self):
        g = Graph([v, w, x], [vw, vx])
        assert sorted(g.out_edges(v)) == sorted([vw, vx])
        assert g.out_edges(w) == [vw, ]
        assert g.out_edges(x) == [vx, ]

    def test_remove_edge(self):
        g = Graph([v, w, x], [vw, vx])
        g.remove_edge(vx)
        assert g == Graph([v, w, x], [vw])
        g.remove_edge(wv)  # backwards vw
        assert g == Graph([v, w, x], [])

    def test_remove_edge_notthere(self):
        g = Graph([v, w, x], [vw, vx])
        g.remove_edge(wx)
        assert sorted(g.vertices()) == [v, w, x]
        assert sorted(g.edges()) == [vw, vx]
