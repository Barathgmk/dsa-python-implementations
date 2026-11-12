"""LFUCache: HashMap + frequency -> ordered list buckets. O(1) get/put.

Conventions (the tests rely on these):
  get returns -1 if missing. Ties on frequency evict the least recently used.

Run this file directly to execute the tests at the bottom.
"""


class LFUCache:
    def __init__(self, capacity):
        # TODO: set up internal state
        raise NotImplementedError

    def get(self, key):
        """get"""
        raise NotImplementedError

    def put(self, key, value):
        """Evict least frequent, ties by recency"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_lfu_cache():

    c = LFUCache(2)
    c.put(1, 1); c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)  # evicts 2 (lowest freq)
    assert c.get(2) == -1
    assert c.get(3) == 3
    c.put(4, 4)  # 1 and 3 tie on freq 2; evicts LRU = 1
    assert c.get(1) == -1 and c.get(3) == 3 and c.get(4) == 4
    z = LFUCache(0)
    z.put(1, 1)
    assert z.get(1) == -1


if __name__ == "__main__":
    test_lfu_cache()
    print("LFUCache: all tests passed")
