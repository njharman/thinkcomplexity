'''This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
'''


def sum_plus(t, init):
    '''Concatenates a list of lists into a single list using +='''
    total = init
    for x in t:
        total += x
    return total


def sum_extend(t, init):
    '''Concatenates a list of lists into a single list using list.extend'''
    total = init
    for x in t:
        total.extend(x)
    return total


def sum_sum(t, init):
    '''Concatenates a list of lists into a single list using sum'''
    return sum(t, init)
