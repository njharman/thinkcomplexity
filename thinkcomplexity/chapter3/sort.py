from __future__ import division
from __future__ import print_function

import bisect


def bisection(seq, item):
    '''Find value in sequence.

    :param seq: sorted sequence.
    :param item:
    :return: None or index of item in seq.
    '''
    # Copied from bisect doc page.
    i = bisect.bisect_left(seq, item)
    if i != len(seq) and seq[i] == item:
        return i
    return None


def bisection2(seq, item):
    '''Find value in sequence.

    :param seq: sorted sequence.
    :param item:
    :return: None or index of item in seq.
    '''
    # Norm's try at bisection algo
    start = 0
    end = len(seq) - 1
    while start < len(seq) and end >= 0:
        mid = ((end - start) // 2) + start
        if item < seq[mid]:
            end = mid - 1
        elif item > seq[mid]:
            start = mid + 1
        else:
            return mid
    return None
