Chapter 4 Exercise 2
====================

The following implementation of a BFS contains two performance errors.

What are they?

A: "queue.pop(0)", is front of list O(n) vs O(1) for list.pop() at end of list.
A: "c not in queue", queue is a list. Membership is O(n) vs O(1) for a set.

What is the actual order of growth for this algorithm?
Not sure.


Test this code with a range of graph sizes and check your analysis. Then use a
FIFO implementation to fix the errors and confirm that your algorithm is
linear.

::

  def bfs(top_node, visit):
      """Breadth-first search on a graph, starting at top_node."""
      visited = set()
      queue = [top_node]
      while len(queue):
          curr_node = queue.pop(0)    # Dequeue
          visit(curr_node)            # Visit the node
          visited.add(curr_node)

          # Enqueue non-visited and non-enqueued children
          queue.extend(c for c in curr_node.children
                      if c not in visited and c not in queue)


