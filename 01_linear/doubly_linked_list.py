"""DoublyLinkedList: Doubly linked list with sentinel head/tail. Basis for LRU, deque, browser history.

Conventions (the tests rely on these):
  push_front/push_back return the new node; nodes expose `.val`; pops return values; empty pop -> IndexError.

Run this file directly to execute the tests at the bottom.
"""
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.len = 0


    def push_front(self, x):
        temp = Node(x)

        temp.next = self.head.next
        temp.prev = self.head

        self.head.next.prev = temp
        self.head.next = temp


        self.len += 1

        return temp 

    def push_back(self, x):
        temp = Node(x)

        temp.prev = self.tail.prev
        temp.next = self.tail

        self.tail.prev.next = temp
        self.tail.prev = temp

        self.len += 1

        return temp

    def pop_front(self):
        if self.len == 0:
            raise IndexError("list is empty")

        temp = self.head.next

        self.head.next = temp.next
        temp.next.prev = self.head   

        self.len -= 1



        return temp.value

    def pop_back(self):
        if self.len == 0:
            raise IndexError("list is empty")
        self.len -=1

        temp = self.tail.prev

        self.tail.prev = temp.prev

        temp.prev.next = self.tail


        return temp.value

    def remove_node(self, node):
        if node is None or node == self.head or node == self.tail:
            return None

        node.prev.next = node.next
        node.next.prev = node.prev

        self.len -= 1

        return node.value
            
    

    def move_to_front(self, node):
        if node is None or node == self.head or node == self.tail:
                    return None
        
        node.prev.next = node.next
        node.next.prev = node.prev
        
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        
        
        return node.value

    def __len__(self):
        return self.len

    def __iter__(self):
        curr = self.head.next

        while curr != self.tail:
            yield curr.value
            curr = curr.next


def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_doubly_linked_list():

    d = DoublyLinkedList()
    n2 = d.push_back(2); n1 = d.push_front(1); n3 = d.push_back(3)
    assert list(d) == [1, 2, 3] and len(d) == 3
    assert n2.value == 2
    d.remove_node(n2)
    assert list(d) == [1, 3] and len(d) == 2
    d.move_to_front(n3)
    assert list(d) == [3, 1]
    assert d.pop_back() == 1 and d.pop_front() == 3 and len(d) == 0
    _raises(IndexError, d.pop_front)
    _raises(IndexError, d.pop_back)
    d.push_back(5)
    assert list(d) == [5]


if __name__ == "__main__":
    test_doubly_linked_list()
    print("DoublyLinkedList: all tests passed")
