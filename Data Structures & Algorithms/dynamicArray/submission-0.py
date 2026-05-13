from sortedcontainers import SortedList

class DynamicArray:
    def __init__(self, capacity: int):
        self.arr = list()
        self.capacity = capacity

    def get(self, i: int) -> int:
        if len(self.arr) < i:
            print("Index Out of range")
            return
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if len(self.arr) < i:
            print("Index Out of range")
            return
        self.arr[i] = n
        return 

    def pushback(self, n: int) -> None:
        if self.capacity == len(self.arr):
            self.capacity *= 2
        self.arr.append(n)
        return

    def popback(self) -> int:
        if len(self.arr) < 0:
            print("Empty")
            return
        return self.arr.pop(-1)

    def resize(self) -> None:
        self.capacity *= 2
        return

    def getSize(self) -> int:
        return len(self.arr)

    def getCapacity(self) -> int:
        return self.capacity