"""LRUCache: HashMap + DoublyLinkedList. O(1) get/put.

Conventions (the tests rely on these):
  get returns -1 if missing.

Run this file directly to execute the tests at the bottom.
"""


class LRUCache:
    def __init__(self, capacity):
        # TODO: set up internal state
        raise NotImplementedError

    def get(self, key):
        """get"""
        raise NotImplementedError

    def put(self, key, value):
        """Evict least recently used at capacity"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_lru_cache():

    c = LRUCache(2)
    c.put(1, 1); c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)  # evicts 2
    assert c.get(2) == -1
    c.put(4, 4)  # evicts 1
    assert c.get(1) == -1 and c.get(3) == 3 and c.get(4) == 4
    c.put(3, 33)  # update, no eviction
    assert c.get(3) == 33 and c.get(4) == 4
    one = LRUCache(1)
    one.put(1, 1); one.put(2, 2)
    assert one.get(1) == -1 and one.get(2) == 2


if __name__ == "__main__":
    test_lru_cache()
    print("LRUCache: all tests passed")
