"""SuffixArray: Sorted suffix indices + LCP array (Kasai).

Conventions (the tests rely on these):
  build returns the suffix array. lcp()[i] = LCP of suffixes sa[i-1], sa[i], with lcp[0] = 0. find returns sorted start indices.

Run this file directly to execute the tests at the bottom.
"""
import random


class SuffixArray:
    def __init__(self):
        # TODO: set up internal state
        raise NotImplementedError

    def build(self, s):
        """build"""
        raise NotImplementedError

    def lcp(self):
        """Kasai"""
        raise NotImplementedError

    def find(self, pattern):
        """Binary search"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_suffix_array():

    sa = SuffixArray()
    assert sa.build("banana") == [5, 3, 1, 0, 4, 2]
    assert sa.lcp() == [0, 1, 3, 0, 0, 2]
    assert sa.find("ana") == [1, 3]
    assert sa.find("a") == [1, 3, 5]
    assert sa.find("banana") == [0]
    assert sa.find("xyz") == [] and sa.find("nab") == []
    rng = random.Random(8)
    s = "".join(rng.choice("abc") for _ in range(200))
    sa = SuffixArray()
    assert sa.build(s) == sorted(range(len(s)), key=lambda i: s[i:])
    for pat in ("ab", "abc", "ca", "cc"):
        assert sa.find(pat) == [i for i in range(len(s)) if s.startswith(pat, i)]


if __name__ == "__main__":
    test_suffix_array()
    print("SuffixArray: all tests passed")
