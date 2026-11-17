"""Stack: LIFO stack (backed by dynamic array or linked list).

Run this file directly to execute the tests at the bottom.
"""
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        

class Stack:
    def __init__(self):
        self.head = Node(None)
        self.len = 0 

    def push(self, x):
        self.len += 1  

        dummy = self.head.next
        newItem = Node(x)
        self.head.next = newItem

        newItem.next = dummy

        

    def pop(self):
        if self.is_empty():
            raise IndexError("empty stack")
        self.len -= 1 
        dummy = self.head.next
        self.head.next = dummy.next
        dummy.next = None
        return dummy.value

    def peek(self):
        if self.is_empty():
            raise IndexError("empty stack")
        return self.head.next.value

    def is_empty(self):
        if self.len == 0:
            return True
        else:
            return False

    def __len__(self):
        return self.len

def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_stack():

    s = Stack()
    assert s.is_empty() and len(s) == 0
    for i in (1, 2, 3):
        s.push(i)
    assert s.peek() == 3 and len(s) == 3 and not s.is_empty()
    assert s.pop() == 3 and s.pop() == 2 and s.pop() == 1
    assert s.is_empty()
    _raises(IndexError, s.pop)
    _raises(IndexError, s.peek)


if __name__ == "__main__":
    test_stack()
    print("Stack: all tests passed")
