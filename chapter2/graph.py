'''Code exercise from Think Complexity book.

Copyright 2011 Allen B. Downey.
Modified 2015 by Norman J. Harman Jr.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
'''

from functools import total_ordering


@total_ordering
class Vertex(object):
    '''A node in a graph.'''

    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        '''Returns a string representation of this object that can
        be evaluated as a Python expression.'''
        return 'Vertex(%s)' % repr(self.label)

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
        return 'Graph(%s)' % super(Graph, self).__repr__()

    def add_all_edges(self):
        '''Makes graph complete by adding Edge between all pairs of Vertices.

        Existing Edges are replaced.
        '''
        for v in self.keys():
            for w in self.keys():
                if v == w:
                    continue
                self[v][w] = Edge(v, w)

    def add_vertex(self, v):
        '''Add Vertex "v" to graph.'''
        self[v] = {}

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
