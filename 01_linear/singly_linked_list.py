
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.len = 0

    def push_front(self, x):
        dummy = Node(x)
        dummy.next = self.head.next
        self.head.next = dummy
        self.len += 1

    def push_back(self, x):
        curr = self.head

        while curr.next is not None:
            curr = curr.next

        curr.next = Node(x)
        self.len += 1

    def pop_front(self):
        if self.len == 0:
            raise IndexError("empty list")

        dummy = self.head.next
        self.head.next = dummy.next
        dummy.next = None

        self.len -= 1
        return dummy.value

    def remove(self, x):
        curr = self.head

        while curr.next is not None:
            if curr.next.value == x:
                curr.next = curr.next.next
                self.len -= 1
                return True

            curr = curr.next

        return False

    def find(self, x):
        curr = self.head.next

        while curr is not None:
            if curr.value == x:
                return curr

            curr = curr.next

        return None

    def reverse(self):
        prev = None
        curr = self.head.next

        while curr is not None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        self.head.next = prev

    def has_cycle(self):
        slow = self.head.next
        fast = self.head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True

        return False

    def __len__(self):
        return self.len

    def __iter__(self):
        curr = self.head.next

        while curr is not None:
            yield curr.value
            curr = curr.next


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_singly_linked_list():
    l = SinglyLinkedList()
    assert len(l) == 0 and list(l) == []
    _raises(IndexError, l.pop_front)
    assert not l.has_cycle() and not l.remove(1) and l.find(1) is None

    l.push_back(2); l.push_back(3); l.push_front(1)
    assert list(l) == [1, 2, 3] and len(l) == 3

    # find returns the node (or None)
    assert l.find(2).value == 2 and l.find(9) is None

    assert l.remove(2) and not l.remove(2)
    assert list(l) == [1, 3] and len(l) == 2
    assert l.remove(1) and list(l) == [3]  # remove head element
    l.push_back(4); l.push_back(5)
    assert l.remove(5) and list(l) == [3, 4]  # remove tail element
    l.push_back(6)  # appending after removing the tail must still work
    assert list(l) == [3, 4, 6]

    l.reverse()
    assert list(l) == [6, 4, 3]
    assert l.pop_front() == 6 and list(l) == [4, 3] and len(l) == 2

    e = SinglyLinkedList()
    e.reverse()  # reversing an empty list is a no-op
    assert list(e) == []
    e.push_back(1); e.reverse()
    assert list(e) == [1]

    # cycle detection: build a cycle by hand
    c = SinglyLinkedList()
    for i in range(5):
        c.push_back(i)
    assert not c.has_cycle()
    tail = c.head
    while tail.next is not None:
        tail = tail.next
    tail.next = c.find(2)  # 4 -> 2
    assert c.has_cycle()


if __name__ == "__main__":
    test_singly_linked_list()
    print("SinglyLinkedList: all tests passed")
