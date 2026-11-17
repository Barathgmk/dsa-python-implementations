"""DynamicArray: Resizable array (amortized O(1) append). Use a fixed-size backing list; double capacity when full.

Run this file directly to execute the tests at the bottom.
"""


class DynamicArray:
    def __init__(self, capacity = 5):
        if capacity < 1:
            raise ValueError("Capacity must be positive")

        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity

    def append(self, x):
        """Add to end"""
        if self.size == self.capacity:
            self._resize(self.capacity * 2)

        self.arr[self.size] = x
        self.size += 1

    def insert(self, i, x):
        """Insert at index, shift right"""
        if i < 0 or i > self.size:
            raise IndexError("Index out of bounds")

        if self.size == self.capacity:
            self._resize(self.capacity * 2)

        for j in range(self.size, i, -1):
            self.arr[j] = self.arr[j - 1]

        self.arr[i] = x
        self.size += 1

    def pop(self, i=-1):
        """Remove and return element at index"""
        if self.size == 0:
            raise IndexError("Pop from empty array")

        if i == -1:
            i = self.size - 1

        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")

        value = self.arr[i]

        for j in range(i, self.size - 1):
            self.arr[j] = self.arr[j + 1]

        self.size -= 1
        self.arr[self.size] = 0

        return value

    def get(self, i):
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")

        return self.arr[i]

    def set(self, i, x):
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")

        self.arr[i] = x

    def __len__(self):
        return self.size

    def _resize(self, cap):
        """Copy into new backing store"""
        new_arr = [0] * cap

        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr
        self.capacity = cap



def _raises(exc, fn, *args):
    try:
        fn(*args)
    except exc:
        return
    raise AssertionError(f"expected {exc.__name__}")


def test_dynamic_array():

    a = DynamicArray()
    for i in range(100):
        a.append(i)
    assert len(a) == 100 and a.get(0) == 0 and a.get(99) == 99
    a.insert(0, -1)
    assert a.get(0) == -1 and a.get(1) == 0 and len(a) == 101
    a.insert(len(a), 500)
    assert a.get(len(a) - 1) == 500
    assert a.pop() == 500
    assert a.pop(0) == -1 and a.get(0) == 0
    a.set(5, "x")
    assert a.get(5) == "x"
    _raises(IndexError, a.get, len(a))
    _raises(IndexError, a.get, -1)
    _raises(IndexError, DynamicArray().pop)


if __name__ == "__main__":
    test_dynamic_array()
    print("DynamicArray: all tests passed")
