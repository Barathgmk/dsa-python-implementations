"""Deque: Double-ended queue (doubly linked list or circular array).

Run this file directly to execute the tests at the bottom.
"""

class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None
            


class Deque:
        def __init__(self):
            self.head = Node(None)
            self.tail = Node(None)
            self.head.next = self.tail
            self.tail.prev = self.head
            self.len = 0


        def push_front(self, x):
            newN = Node(x)

            newN.next = self.head.next
            newN.prev = self.head

            self.head.next.prev = newN
            self.head.next = newN
            self.len += 1


        def push_back(self, x):
            newN = Node(x)

            

            newN.prev = self.tail.prev
            newN.next = self.tail

            self.tail.prev.next = newN
            self.tail.prev = newN
            self.len += 1 
            
            
        def pop_front(self):
            if self.len == 0:
                raise IndexError("pop from an empty queue")
            if self.head.next == self.tail:
                return None
            temp  = self.head.next 
            self.head.next = temp.next
            temp.next.prev = temp.prev

            self.len -= 1
            return temp.value   
        


        def pop_back(self):
            if self.len == 0:
                            raise IndexError("pop from an empty queue")
            if self.tail.prev == self.head:
                return None

            temp = self.tail.prev
            self.tail.prev = temp.prev
            temp.prev.next = temp.next

            self.len -= 1
            return temp.value


        def peek_front(self):
            if self.len ==0:
                return None
            return self.head.next.value

        def peek_back(self):
            if self.len == 0:
                return None
            return self.tail.prev.value

        def __len__(self):
            return self.len


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_deque():

    d = Deque()
    d.push_back(2); d.push_back(3); d.push_front(1)
    assert d.peek_front() == 1 and d.peek_back() == 3 and len(d) == 3
    assert d.pop_front() == 1 and d.pop_back() == 3 and d.pop_back() == 2
    _raises(IndexError, d.pop_front)
    _raises(IndexError, d.pop_back)
    for i in range(100):
        d.push_back(i)
    assert [d.pop_front() for _ in range(100)] == list(range(100))
    for i in range(100):
        d.push_front(i)
    assert [d.pop_back() for _ in range(100)] == list(range(100))


if __name__ == "__main__":
    test_deque()
    print("Deque: all tests passed")
