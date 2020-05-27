'''This module contains code from "Think Python" by Allen B. Downey

http://thinkpython.com
Copyright 2012 Allen B. Downey
Modified 2015 Norman J. Harman jr.
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
'''
from __future__ import print_function

import os
import matplotlib.pyplot as pyplot


def etime():
    '''Returns the sum of user and system time.'''
    user, sys, chuser, chsys, real = os.times()
    return user + sys


def fit(ns, ts, exp=1.0, index=-1):
    '''Fits a curve with the given exponent.

    Use the given index as a reference point, and scale all other
    points accordingly.
    '''
    nref = ns[index]
    tref = ts[index]
    tfit = list()
    for n in ns:
        ratio = float(n) / nref
        t = ratio**exp * tref
        tfit.append(t)
    return tfit


def make_fig(names, nss, tss, scale='log', exp=1.0, filename=None):
    '''
    exp: exponent (slope) for the fitted curve
    '''
    pyplot.clf()
    pyplot.xscale(scale)
    pyplot.yscale(scale)
    pyplot.title('')
    pyplot.xlabel('n')
    pyplot.ylabel('run time (s)')
    colors = ['blue', 'orange', 'green', 'red', 'black']
    for name, ns, ts, color in zip(names, nss, tss, colors):
        tfit = fit(ns, ts, exp)
        pyplot.plot(ns, tfit, color='0.7', linewidth=2, linestyle='dashed')
        pyplot.plot(ns, ts, label=name, color=color, linewidth=3)
    pyplot.legend(loc=4)
    if filename:
        pyplot.savefig('%s.svg' % (filename, ))
    else:
        pyplot.show()


def time(testee, factor):
    '''Times the given function with a range of values for n.

    :param testee: f.setup(n) f.time(n)
    Returns a list of ns and a list of run times.
    '''
    # test (f) over a range of values for (n)
    ns = list()
    ts = list()
    for i in range(2, 25):
        n = factor * i
        testee.setup(n)
        start = etime()
        testee.time(n)
        end = etime()
        t = end - start
        print(n, t)
        ns.append(n)
        ts.append(t)
    return ns, ts


def tf_append(func):
    '''Return test function.
    :param func: f(lol, []) list of lists of length (n)
    '''
    def test(n):
        t = [[1]] * n
        func(t, [])
    return test


def tf_add(cls):
    def test(n):
        m = cls()
        for i in range(n):
            m.add(n, n)
    return test


if __name__ == '__main__':
    # Depending on which function we are testing, we need to
    # use a different order of magnitude for (n).

    # from listsum import sum_plus, sum_extend, sum_sum
    # funcs = list()
    # nss = list()
    # tss = list()
    # for func in [sum_extend, sum_plus]:
    #     ns, ts = time(tf_append(func), 100000)
    #     funcs.append(func.__name__)
    #     nss.append(ns)
    #     tss.append(ns)
    # make_fig(funcs, nss, tss, exp=1.0, filename='loglistsum1')
    #
    # ns, ts = time(tf_append(sum_sum), 1000)
    # make_fig(['sum_sum'], [ns], [ts], exp=2.0, filename='loglistsum2')

    from mymap import LinearMap, BetterMap, HashMap

    print('linear')
    ns, ts = time(tf_add(LinearMap), 10000)
    make_fig(['linearmap.add'], [ns], [ts], exp=1.0, filename='add_linearmap')
    print('better')
    ns, ts = time(tf_add(BetterMap), 10000)
    make_fig(['bettermap.add'], [ns], [ts], exp=1.0, filename='add_bettermap')
    print('hash')
    ns, ts = time(tf_add(HashMap), 1000)
    make_fig(['hashmap.add'], [ns], [ts], exp=1.0, filename='add_hashmap')

    # print('linear')
    # ns, ts = time(tf_get(LinearMap), 10000)
    # make_fig(['linearmap.get'], [ns], [ts], exp=1.0, filename='get_linearmap')
    # print('better')
    # ns, ts = time(tf_get(BetterMap), 10000)
    # make_fig(['bettermap.get'], [ns], [ts], exp=1.0, filename='get_bettermap')
    # print('hash')
    # ns, ts = time(tf_get(HashMap), 1000)
    # make_fig(['hashmap.get'], [ns], [ts], exp=1.0, filename='get_hashmap')

    # t = HashMap()
    # for n in range(15):
    #     t.add(n, None)
    # for i, l in enumerate(t.maps):
    #     print(' #%i len'%i, len(l), l)
    # print('maps', len(t.maps))
