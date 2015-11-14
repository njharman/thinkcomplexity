'''Code exercise from Chapter 4 of "Think Complexity" by Allen B. Downey.
'''
from __future__ import print_function


class FIFO(object):
    '''First In First Out queue.'''
    def __init__(self):
        self._head = 0
        self._tail = 0
        self._data = dict()

    def __str__(self):
        return self.__class__.__name__

    def __len__(self):
        return len(self._data)

    def append(self, item):
        '''Add item to fifo.'''
        self._data[self._head] = item
        self._head += 1

    def pop(self):
        '''Return oldest item in fifo.'''
        if self._tail == self._head:
            raise IndexError('pop from empty %s' % self.__class__.__name__)
        item = self._data[self._tail]
        del self._data[self._tail]
        self._tail += 1
        return item
