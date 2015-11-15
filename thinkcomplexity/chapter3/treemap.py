'''Code exercise from Chap3 Think Complexity book.

Copyright 2011 Allen B. Downey.
Modified 2015 by Norman J. Harman Jr.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
'''
from __future__ import print_function

import string


class Node(object):
    __slots__ = ('red', 'left', 'right', 'parent', 'key', 'value')

    def __init__(self, red, left, right, parent, key, value):
        self.red = red
        self.left = left
        self.right = right
        self.parent = parent
        self.key = key
        self.value = value

    def __repr__(self):
        return '%s %s l:%s r:%s p:%s ' % (self, ['blk', 'red'][self.red], self.left, self.right, self.parent)

    def __str__(self):
        return '%s->%s' % (self.key, self.value)

    @property
    def isred(self):
        return self.red

    @property
    def isblack(self):
        return not self.red

    @property
    def grand(self):
        if self.parent:
            return self.parent.parent

    @property
    def uncle(self):
        if self.grand:
            if self.grand.left == self.parent:
                return self.grand.right
            else:
                return self.grand.left


class TreeMap(object):
    '''An implementation of a hashtable api using Red-Black Trees.

    add() and get() should be O(logn).

    RBTree Properties
    -----------------
    1. A node is either red or black.
    2. The root is black.
    3. All leaves (NIL) are black.
    4. If a node is red, then both its children are black.
    5. Every path from a given node to any of its descendant NIL nodes
       contains the same number of black nodes. The uniform number of black
       nodes in the paths from root to leaves is called the black-height of
       the red-black tree.
    '''
    nil = Node(red=False, left=None, right=None, parent=None, key=None, value=None)

    def __init__(self):
        self.root = self.nil

    def __str__(self):
        return '%s' % self.__class__.__name__

    def _rotate_left(self, node):
        n = node.right
        node.right = n.left
        if n.left != self.nil:
            n.left.parent = node
        n.parent = node.parent
        if node.parent == self.nil:
            self.root = n
        elif node == node.parent.left:
            node.parent.left = n
        else:
            node.parent.right = n
        n.left = node
        node.parent = n

    def _rotate_right(self, node):
        n = node.left
        node.left = n.right
        if n.right != self.nil:
            n.right.parent = node
        n.parent = node.parent
        if node.parent == self.nil:
            self.root = n
        elif node == node.parent.right:
            node.parent.right = n
        else:
            node.parent.left = n
        n.right = node
        node.parent = n

    def _normalize(self, node):
        '''Fix Red-Black tree properties.'''
        # Root node
        if node == self.root:
            node.red = False
        # Black parent
        elif node.parent.isblack:
            return
        # Red parent, Red uncle
        elif node.uncle and node.uncle.isred:
            node.parent.red = False
            node.uncle.red = False
            node.grand.red = True
            self._normalize(node.grand)
        # Red parent, Black uncle
        elif node.uncle and node.uncle.isblack:
            # N is added to right of left child of grandparent
            if node == node.parent.right and node.parent == node.grand.left:
                p = node.parent
                self._rotate_left(p)
                node = p
            # N is added to left of right child of grandparent
            elif node == node.parent.left and node.parent == node.grand.right:
                p = node.parent
                self._rotate_right(p)
                node = p
            # Above if/elif needs to fall through to folowing if/elif.
            # N is added to left of left child of grandparent
            node.parent.red = False
            node.grand.red = True
            # if node == node.parent.left and node.parent == node.grand.left:
            if node == node.parent.left:
                self._rotate_right(node.grand)
            # N is added to right of right child of grandparent
            # elif node == node.parent.right and node.parent == node.grand.right:
            else:
                self._rotate_left(node.grand)

    def add(self, k, v):
        '''Add value v at key k.'''
        # Find what node(parent) to attach it to.
        n = parent = self.root
        while n != self.nil:
            parent = n
            if k < n.key:
                n = n.left
            elif k > n.key:
                n = n.right
            else:  # Same key, replace value.
                n.value = v
                return
        # and put it there.
        newnode = Node(red=True, left=self.nil, right=self.nil, parent=parent, key=k, value=v)
        if parent == self.nil:
            self.root = newnode
        elif k <= parent.key:
            parent.left = newnode
        else:
            parent.right = newnode
        self._normalize(newnode)

    def get(self, k):
        '''Returns value for key (k) or raises KeyError if no such key.'''
        n = self.root
        while n != self.nil:
            if k < n.key:
                n = n.left
            elif k > n.key:
                n = n.right
            else:
                return n.value
        raise KeyError

    def walk(self, node=None, i=0):
        '''Debug'''
        if node:
            if node.key is None:
                print(' ' * i, 'nil')
                return
            print(' ' * i, repr(node))
            self.walk(node.left, i + 1)
            self.walk(node.right, i)


def check_invariants(tree):
    '''Adapted from http://code.activestate.com/recipes/576817-red-black-tree/
    :return: True iff satisfies all criteria to be red-black tree.
    '''
    def is_red_black_node(node):
        '@return: num_black, is ok'
        if tree.nil.isred:
            print('red nil: %r' % (tree.nil, ))
            return 0, False
        for field in ('left', 'right', 'parent', 'key', 'value'):
            if getattr(tree.nil, field) is not None:
                print('messed up nil: %r' % (tree.nil, ))
                return 0, False
        # Check has left and right.
        if not ((node.left and node.right) or (not node.left and not node.right)):
            print('nodes: %r' % (node, ))
            return 0, False
        # Check leaves are black.
        if not node.left and not node.right and node.isred:
            print('red leaves: %r' % (node, ))
            return 0, False
        # If node is red, check children are black.
        if node.isred and node.left and node.right:
            if node.left.isred or node.right.isred:
                print('red nodes need black children %r' % (node, ))
                return 0, False
        # Descend tree and check black counts are balanced.
        if node.left and node.right:
            # Check children's parents are correct.
            if tree.nil != node.left and node != node.left.parent:
                print('parent1 %r' % (node, ))
                return 0, False
            if tree.nil != node.right and node != node.right.parent:
                print('parent2 %r' % (node, ))
                return 0, False
            # Check children are ok
            left_counts, left_ok = is_red_black_node(node.left)
            if not left_ok:
                print('chillin1 %r' % (node, ))
                return 0, False
            right_counts, right_ok = is_red_black_node(node.right)
            if not right_ok:
                print('chillin2 %r' % (node, ))
                return 0, False
            # Check children's counts are ok.
            if left_counts != right_counts:
                print('chillin counts %r' % (node, ))
                return 0, False
            return left_counts, True
        else:
            return 0, True
    num_black, is_ok = is_red_black_node(tree.root)
    return is_ok and not tree.root.isred


def write_tree_as_dot(t, fh, show_nil=False):
    '''Write the tree in the dot language format to f.
    Adapted from http://code.activestate.com/recipes/576817-red-black-tree/
    '''
    def visit_node(node):
        print('  %s [label="%s", color="%s"];' % (node.key, node, ['black', 'red'][node.red]), file=fh)
        if node.left and (node.left != t.nil or show_nil):
            visit_node(node.left)
            print('  %s -> %s ;' % (node.key, node.left.key), file=fh)
        if node.right and (node.right != t.nil or show_nil):
            visit_node(node.right)
            print('  %s -> %s ;' % (node.key, node.right.key), file=fh)

    print('// Created by rbtree.write_dot()', file=fh)
    print('digraph red_black_tree {', file=fh)
    visit_node(t.root)
    print('}', file=fh)


def graph_tree(t, filename):
    '''Write the tree as a .dot and SVG file.
    Adapted from http://code.activestate.com/recipes/576817-red-black-tree/
    '''
    import os
    os.system('rm -f %s.dot %s.svg' % (filename, filename))
    with open('%s.dot' % filename, 'w') as fh:
        write_tree_as_dot(t, fh)
    os.system('dot %s.dot -Tsvg -o %s.svg' % (filename, filename))


if __name__ == '__main__':
    import random

    def map_me(name, size=26):
        t = TreeMap()
        pairs = list(enumerate(random.choice(string.ascii_lowercase) for i in range(size)))
        random.shuffle(pairs)
        for k, v in pairs:
            t.add(k, v)
        graph_tree(t, name)
        print(name, t, check_invariants(t))

    map_me('tree1', 26)
    map_me('tree2', 50)
