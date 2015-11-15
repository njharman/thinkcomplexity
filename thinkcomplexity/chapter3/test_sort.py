from __future__ import absolute_import

import pytest

from thinkcomplexity.chapter3.sort import bisection, bisection2


def test_bisection():
    test = range(1, 6)
    assert 0 == bisection(test, 1)
    assert 2 == bisection(test, 3)
    assert 4 == bisection(test, 5)
    assert None == bisection(test, 0)
    assert None == bisection(test, 10)
    assert None == bisection(test, 10)
    assert None == bisection([], 0)
    test = range(-4, 6)
    assert 0 == bisection(test, -4)
    assert 3 == bisection(test, -1)
    assert 4 == bisection(test, 0)
    assert 5 == bisection(test, 1)
    assert None == bisection(test, -5)


def test_bisection2():
    test = range(1, 6)
    assert 0 == bisection2(test, 1)
    assert 2 == bisection2(test, 3)
    assert 4 == bisection2(test, 5)
    assert None == bisection2(test, 0)
    assert None == bisection2(test, 10)
    assert None == bisection2(test, 10)
    assert None == bisection2([], 0)
    test = range(-4, 6)
    assert 0 == bisection(test, -4)
    assert 3 == bisection(test, -1)
    assert 4 == bisection(test, 0)
    assert 5 == bisection(test, 1)
    assert None == bisection(test, -5)
