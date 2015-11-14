import pytest

from .fifo import FIFO


class TestFIFO(object):
    def test_basic(self):
        t = FIFO()
        str(t)

    def test_len(self):
        t = FIFO()
        assert 0 == len(t)
        t.append(0)
        assert 1 == len(t)
        t.append(0)
        assert 2 == len(t)
        t.pop()
        assert 1 == len(t)

    def test_pop_empty(self):
        t = FIFO()
        with pytest.raises(IndexError):
            t.pop()
        t.append(None)
        t.pop()
        with pytest.raises(IndexError):
            t.pop()

    def test_order(self):
        t = FIFO()
        t.append('cat')
        t.append('dog')
        assert 'cat' == t.pop()
        assert 'dog' == t.pop()

    def test_lots(self):
        t = FIFO()
        for i in range(1000):
            t.append(i)
        for i in range(500):
            assert i == t.pop()
        for i in range(1000, 1500):
            t.append(i)
            assert i - 500 == t.pop()
