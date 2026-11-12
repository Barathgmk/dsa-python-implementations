"""Queue: FIFO queue (linked list or two-stack implementation).

Run this file directly to execute the tests at the bottom.
"""


class Queue:
    def __init__(self):
        # TODO: set up internal state
        raise NotImplementedError

    def enqueue(self, x):
        """enqueue"""
        raise NotImplementedError

    def dequeue(self):
        """dequeue"""
        raise NotImplementedError

    def peek(self):
        """peek"""
        raise NotImplementedError

    def is_empty(self):
        """is_empty"""
        raise NotImplementedError

    def __len__(self):
        """__len__"""
        raise NotImplementedError


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_queue():

    q = Queue()
    assert q.is_empty()
    for i in (1, 2, 3):
        q.enqueue(i)
    assert q.peek() == 1 and len(q) == 3
    assert q.dequeue() == 1 and q.dequeue() == 2
    q.enqueue(4)
    assert q.dequeue() == 3 and q.dequeue() == 4 and q.is_empty()
    _raises(IndexError, q.dequeue)
    _raises(IndexError, q.peek)


if __name__ == "__main__":
    test_queue()
    print("Queue: all tests passed")
