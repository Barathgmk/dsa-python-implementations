"""Bitset: Compact set of ints stored in bits (use int or bytearray).

Run this file directly to execute the tests at the bottom.
"""


class Bitset:
    def __init__(self, n):
        # TODO: set up internal state
        raise NotImplementedError

    def set(self, i):
        """set"""
        raise NotImplementedError

    def clear(self, i):
        """clear"""
        raise NotImplementedError

    def test(self, i):
        """test"""
        raise NotImplementedError

    def flip(self, i):
        """flip"""
        raise NotImplementedError

    def count(self):
        """Popcount"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_bitset():

    b = Bitset(100)
    assert b.count() == 0 and not b.test(5)
    b.set(3); b.set(64); b.set(99)
    assert b.test(3) and b.test(64) and b.test(99) and not b.test(4)
    assert b.count() == 3
    b.set(3)
    assert b.count() == 3
    b.clear(64)
    assert not b.test(64) and b.count() == 2
    b.flip(10)
    assert b.test(10)
    b.flip(10)
    assert not b.test(10)
    b.clear(0)
    assert b.count() == 2


if __name__ == "__main__":
    test_bitset()
    print("Bitset: all tests passed")
