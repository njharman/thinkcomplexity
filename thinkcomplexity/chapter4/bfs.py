from thimnkcomplexity.chapter2.graph import RandomGraph, make_vertices


def bfs(root, visit): '''Breadth-first search on a graph, starting at node.'''
visited = set() queue = [root, ] while len(queue): node = queue.pop(0)
visit(node) visited.add(node) queue.extend(n for n in node.children if n not
        in visited and n not in queue)


class TestBFS(object):
    def setup(self, n):
        vertices = make_vertices(n)
        self.root = vertices[0]
        self.graph = RandomGraph(vertices)
        self.graph.add_random_edges(.2)

    def time(self, n):
        bfs(self.root, id)


if __name__ == '__main__':
    from chapter3.plottimes import time, make_fig

    foo = TestBFS()

    ns, ts = time(foo, 10)
    make_fig(['RandomGraph.bfs'], [ns], [ts], exp=1.0, filename='bfs_randomgraph')
