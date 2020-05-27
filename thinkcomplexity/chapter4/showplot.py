'''Code exercise from Chapter 4 of "Think Complexity" by Allen B. Downey.
'''
from __future__ import print_function
from __future__ import absolute_import

import matplotlib.pyplot as pyplot

from thinkcomplexity.chapter4.smallworldgraph import make_vertices, SmallWorldGraph


if __name__ == '__main__':
    vertices = make_vertices(1000)
    g = SmallWorldGraph(vertices)
    g.rewire(0.01)

    ps = [0.01, ]
    cs = [g.clustering_coefficient(), ]

    pyplot.clf()
    pyplot.title('exercise 4')
    pyplot.xscale('log')
    pyplot.xlabel('p')
    pyplot.ylabel('')
    pyplot.plot(ps, cs, label='C(p) / C(0)', color='blue', linewidth=3)
    pyplot.legend(loc=4)
    filename = None
    if filename:
        pyplot.savefig('%s.svg' % (filename, ))
    else:
        pyplot.show()
