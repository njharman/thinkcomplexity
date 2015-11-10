#!/usr/bin/env python
'''Chapter 2 Exercise 6 Think Complexity book by Allen B. Downey.
'''
from __future__ import print_function

import sys

from graph import RandomGraph, Vertex, labels


def fraction_connected(n, p, count=20):
    '''Return fraction of RandomGraphs G(n,p) that are connected.'''
    vertices = [Vertex(c) for c in labels][:n]
    connected = 0.0
    for i in range(count):
        g = RandomGraph(vertices)
        g.add_random_edges(p)
        if g.is_connected():
            connected += 1
    return connected / count


if __name__ == '__main__':
    n = int(sys.argv[1])
    p = float(sys.argv[2])
    connected = fraction_connected(n, p)
    print('%0.2f connected random graphs for n=%i and p=%f' % (connected * 100, n, p))
