"""BloomFilter: Probabilistic membership: false positives possible, no false negatives.

Run this file directly to execute the tests at the bottom.
"""


class BloomFilter:
    def __init__(self, size, num_hashes):
        # TODO: set up internal state
        raise NotImplementedError

    def add(self, x):
        """add"""
        raise NotImplementedError

    def might_contain(self, x):
        """might_contain"""
        raise NotImplementedError

    def _hashes(self, x):
        """k hash functions"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_bloom_filter():

    bf = BloomFilter(10000, 3)
    present = [f"item{i}" for i in range(1000)]
    for x in present:
        bf.add(x)
    assert all(bf.might_contain(x) for x in present)  # no false negatives, ever
    false_pos = sum(bf.might_contain(f"other{i}") for i in range(1000))
    assert false_pos < 100, f"false positive rate too high: {false_pos}/1000"
    assert not BloomFilter(100, 3).might_contain("anything")


if __name__ == "__main__":
    test_bloom_filter()
    print("BloomFilter: all tests passed")
