"""MonotonicQueue: Deque kept monotonic. Use for sliding window maximum.

Run this file directly to execute the tests at the bottom.
"""


class MonotonicQueue:
    def __init__(self):
        # TODO: set up internal state
        raise NotImplementedError

    def push(self, x):
        """push"""
        raise NotImplementedError

    def pop(self, x):
        """Remove x if it is the front"""
        raise NotImplementedError

    def max(self):
        """max"""
        raise NotImplementedError

    @staticmethod
    def sliding_window_max(nums, k):
        """Static helper"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_monotonic_queue():

    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    assert MonotonicQueue.sliding_window_max(nums, 3) == [3, 3, 5, 5, 6, 7]
    assert MonotonicQueue.sliding_window_max(nums, 1) == nums
    assert MonotonicQueue.sliding_window_max([4, 4, 4], 2) == [4, 4]
    # manual use of the instance API
    q = MonotonicQueue()
    k, res = 3, []
    for i, x in enumerate(nums):
        q.push(x)
        if i >= k:
            q.pop(nums[i - k])
        if i >= k - 1:
            res.append(q.max())
    assert res == [3, 3, 5, 5, 6, 7]


if __name__ == "__main__":
    test_monotonic_queue()
    print("MonotonicQueue: all tests passed")
