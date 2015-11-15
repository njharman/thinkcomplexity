'''Code exercise from Chap3 Think Complexity book.

Copyright 2011 Allen B. Downey.
Modified 2015 by Norman J. Harman Jr.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
'''

import string


class LinearMap(object):
    '''A simple implementation of a map using a list of tuples
    where each tuple is a key-value pair.
    '''

    def __init__(self):
        self.items = list()

    def __str__(self):
        return 'LinearMap(%s)' % self.items

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        '''Iterate over items being held, return 1 item per call.'''
        for item in self.items:
            yield item

    def add(self, key, value):
        '''Add a new item that maps from key (k) to value (v).
        Assumes that they keys are unique.
        '''
        self.items.append((key, value))

    def get(self, k):
        '''Look up the key (k) and returns the corresponding value,
        or raises KeyError if the key is not found.
        '''
        for key, value in self.items:
            if key == k:
                return value
        raise KeyError


class BetterMap(object):
    '''A faster implementation of a map using a list of LinearMaps
    and the built-in function hash() to determine which LinearMap
    to put each key into.
    '''

    def __init__(self, n=100):
        '''Append (n) LinearMaps onto (self).'''
        self.maps = [LinearMap() for i in range(n)]

    def __str__(self):
        return 'BetterMap(%i)' % len(self)

    def __len__(self):
        '''Number of linear maps being held.'''
        return len(self.maps)

    def __iter__(self):
        '''Iterate over maps being held, return 1 map per call.'''
        for m in self.maps:
            yield m

    def find_map(self, key):
        '''Find the right LinearMap for key (k).'''
        index = hash(key) % len(self.maps)
        return self.maps[index]

    def add(self, key, value):
        '''Add a new item to the appropriate LinearMap for key (k).'''
        m = self.find_map(key)
        m.add(key, value)

    def get(self, key):
        '''Find the right LinearMap for key (k) and looks up (k) in it.'''
        m = self.find_map(key)
        return m.get(key)


class HashMap(object):
    '''An implementation of a hashtable using a BetterMap
    that grows so that the number of items never exceeds the number
    of LinearMaps.

    The amortized cost of add should be O(1) provided that the
    implementation of sum in resize is linear.
    '''

    def __init__(self):
        '''Starts with 2 LinearMaps and 0 items.'''
        self.maps = BetterMap(10)
        self.num = 0

    def __str__(self):
        return 'HashMap(%s)' % self.maps

    def get(self, k):
        '''Looks up the key (k) and returns the corresponding value,
        or raises KeyError if the key is not found.
        '''
        return self.maps.get(k)

    def add(self, k, v):
        '''Resize the map if necessary and adds the new item.'''
        if self.num >= len(self.maps):
            self.resize()
        self.maps.add(k, v)
        self.num += 1

    def resize(self):
        '''Makes a new map, twice as big, and rehashes the items.'''
        new_maps = BetterMap(self.num * 2)
        for m in self.maps:
            for k, v in m:
                new_maps.add(k, v)
        self.maps = new_maps


if __name__ == '__main__':
    m = HashMap()
    s = string.ascii_lowercase
    for k, v in enumerate(s):
        m.add(k, v)
    for k in range(len(s)):
        print k, m.get(k)
