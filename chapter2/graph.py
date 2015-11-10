'''Code exercise from Think Complexity book.

Copyright 2011 Allen B. Downey.
Modified 2015 by Norman J. Harman Jr.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
'''
from __future__ import print_function

import math
import random
import itertools
from functools import total_ordering


class GraphException(Exception):
    pass


@total_ordering
class Vertex(object):
    '''A node in a graph.'''

    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        '''Returns a string representation of this object that can
        be evaluated as a Python expression.'''
        return '%s(%s)' % (self.__class__.__name__, repr(self.label))

    __str__ = __repr__

    def __lt__(self, other):
        '''By label then arbitary order.'''
        return (self.label, id(self)) < (other.label, id(other))


class Edge(tuple):
    '''A pair of two Vertices. Undirected.'''

    def __new__(cls, *vs):
        '''The Edge constructor takes two vertices.'''
        if len(vs) != 2:
            raise ValueError('Edges must connect exactly two vertices.')
        return tuple.__new__(cls, vs)

    def __repr__(self):
        '''Return a string representation of this object that can
        be evaluated as a Python expression.'''
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__

    def __eq__(self, other):
        '''Edges with same Vertices are equal.'''
        return set(self) == set(other)

    def __hash__(self):
        '''Equal object must have same hash. So, we normalize by sorting our Vertices.'''
        return hash(tuple(sorted(self)))


class Graph(dict):
    '''Simple undirected graph.

    A Graph is a dictionary of dictionaries.
    The outer dictionary maps from a vertex to an inner dictionary.  The inner dictionary maps from other vertices to edges.

    For vertices a and b, graph[a][b] maps
    to the edge that connects a->b, if it exists.'''

    def __init__(self, vs=[], es=[]):
        '''Create new graph.

        vs: list of Vertices;
        es: list of Edges.
        '''
        for v in vs:
            self.add_vertex(v)
        for e in es:
            self.add_edge(e)

    def __str__(self):
        return super(Graph, self).__str__()

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, super(Graph, self).__repr__())

    def _remove_all_edges(self):
        '''Remove all edges from graph.'''
        vertices = list(self.keys())
        for vertex in vertices:
            self[vertex] = dict()

    # TODO: Should be called make_complete.
    def add_all_edges(self):
        '''Makes graph complete by adding Edge between all pairs of Vertices.

        WARNING: All existing Edges are removed.
        '''
        self._remove_all_edges()
        # Is there faster than On^2 algo for all possible pairs of sequence?
        # Assume stdlib would use it... Takes 11s with 1000 vertex graph.
        for v1, v2 in itertools.combinations(self.keys(), 2):
            self.add_edge(Edge(v1, v2))

    # TODO: Should be called make_regular.
    def add_regular_edges(self, degree):
        '''Makes degree'th regular graph. That is each vertex has same number of neighbors.

        WARNING: All existing Edges are removed.

        For d regular graph of order o to exist, o >= d+1 and o*d is even.

        if degree = 2m connect to m neighbors each side.
        if degree = 2m+1 connect to m neighbors each side and to vertex directly opposite.
        '''
        def normalize_index(i):
            if i >= vertex_count:
                i -= vertex_count
            return i

        self._remove_all_edges()
        if degree < 0:
            raise ValueError('Negative (%i) degree makes no sense.' % (degree, ))
        if degree == 0:  # Just unconnected vertices.
            return
        vertex_count = len(self)
        if vertex_count <= degree:
            raise GraphException('Graph of degree %i must have at least degree+1 vertices.' % (degree, ))
        if (vertex_count * degree) % 2 != 0:
            raise GraphException('Graph of degree %i with %i vertices is not possible.' % (degree, vertex_count))
        vertices = self.vertices()
        m = int(math.floor(degree / 2.0))
        for i in range(vertex_count):
            # List of indexes of the m vertices before and after i.
            for n in itertools.chain(range(i - m, i), range(1 + i, 1 + i + m)):
                n = normalize_index(n)
                self.add_edge(Edge(vertices[i], vertices[n]))
            # If odd degree, add extra vertex opposite.
            if degree != m * 2:
                n = i - (vertex_count // 2)
                n = normalize_index(n)
                self.add_edge(Edge(vertices[i], vertices[n]))

    def is_connected(self):
        '''Is there a path from every node to every other node.'''
        if len(self) == 0:
            return True
        # Prime queue with "first vertex.
        # Pop a vertex from queue
        #   add all it's non-marked neighbors to queue.
        #   mark them as visited.
        #   repeat until queue empty.
        # Graph is connected if all vertices are marked.
        to_visit = list()
        marked = set()
        to_visit.append(self.vertices()[0])
        marked.add(to_visit[0])
        while to_visit:
            v = to_visit.pop()
            for v in self.out_vertices(v):
                if v not in marked:
                    marked.add(v)
                    to_visit.append(v)
        for v in self.vertices():
            if v not in marked:
                return False
        return True

    def add_vertex(self, v):
        '''Add Vertex "v" to graph.'''
        self[v] = dict()

    def add_edge(self, e):
        '''Add undirected Edge "e" to graph.

        If there is already an edge connecting these Vertices, the
        new edge replaces it.
        '''
        v, w = e
        self[v][w] = e
        self[w][v] = e

    def remove_edge(self, e):
        '''Remove any reference Edge "e".'''
        v, w = e
        try:
            del self[v][w]
        except KeyError:
            pass
        try:
            del self[w][v]
        except KeyError:
            pass

    def get_edge(self, v, w):
        '''Return edge between Vertices v,w or None if no such edge.'''
        vertex = self.get(v, None)
        if not vertex:
            return None
        return vertex.get(w, None)

    def vertices(self):
        '''Return list of Vertices.'''
        return list(self.keys())

    def edges(self):
        '''Return list of Edges.'''
        return list(set(e for v in self.values() for e in v.values()))

    def out_vertices(self, v):
        '''Return list of Vertices adjacent to Vertix "v".'''
        try:
            return list(self[v].keys())
        except KeyError:
            return list()

    def out_edges(self, v):
        '''Return a list of Edges connected to Vertex "v".'''
        try:
            return list(set(e for e in self[v].values()))
        except KeyError:
            return list()


class RandomGraph(Graph):
    def add_random_edges(self, p):
        '''Starting with an edgeless graph, add edges at random so that the
        probability is p that there is an edge between any two nodes.

        WARNING: All existing Edges are removed.

        :param p: float 0-1
        '''
        self._remove_all_edges()
        # TODO: Should be binomial distribution.
        # All possible undirected edges, normalized.
        edges = set(tuple(sorted([v1, v2])) for v1 in self for v2 in self if v1 != v2)
        for v1, v2 in edges:
            if random.random() <= p:
                e = Edge(v1, v2)
                self.add_edge(e)
