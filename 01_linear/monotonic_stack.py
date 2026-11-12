"""MonotonicStack: Stack that keeps elements monotonic. Use for next greater element, histogram.

Conventions (the tests rely on these):
  next_greater returns -1 where there is none.

Run this file directly to execute the tests at the bottom.
"""


class MonotonicStack:
    def __init__(self):
        # TODO: set up internal state
        raise NotImplementedError

    def push(self, x):
        """Pop violating elements first"""
        raise NotImplementedError

    @staticmethod
    def next_greater(nums):
        """Static helper: next greater element array"""
        raise NotImplementedError

    @staticmethod
    def largest_rectangle(heights):
        """Largest rectangle in histogram"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_monotonic_stack():

    assert MonotonicStack.next_greater([2, 1, 2, 4, 3]) == [4, 2, 4, -1, -1]
    assert MonotonicStack.next_greater([5, 4, 3]) == [-1, -1, -1]
    assert MonotonicStack.next_greater([]) == []
    assert MonotonicStack.largest_rectangle([2, 1, 5, 6, 2, 3]) == 10
    assert MonotonicStack.largest_rectangle([2, 4]) == 4
    assert MonotonicStack.largest_rectangle([1, 1, 1, 1]) == 4
    assert MonotonicStack.largest_rectangle([]) == 0


if __name__ == "__main__":
    test_monotonic_stack()
    print("MonotonicStack: all tests passed")
