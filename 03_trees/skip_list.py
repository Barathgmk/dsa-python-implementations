"""SkipList: Probabilistic layered linked list, O(log n) expected.

Run this file directly to execute the tests at the bottom.
"""
import random


class SkipList:
    def __init__(self):
        # TODO: set up internal state
        raise NotImplementedError

    def insert(self, x):
        """insert"""
        raise NotImplementedError

    def search(self, x):
        """search"""
        raise NotImplementedError

    def delete(self, x):
        """delete"""
        raise NotImplementedError

    def _random_level(self):
        """_random_level"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_skip_list():

    rng = random.Random(4)
    sl, ref = SkipList(), set()
    for _ in range(2000):
        x = rng.randint(0, 300)
        r = rng.random()
        if r < 0.5:
            sl.insert(x); ref.add(x)
        elif r < 0.8:
            assert bool(sl.delete(x)) == (x in ref); ref.discard(x)
        else:
            assert bool(sl.search(x)) == (x in ref)
    assert all(sl.search(x) for x in ref)


if __name__ == "__main__":
    test_skip_list()
    print("SkipList: all tests passed")
