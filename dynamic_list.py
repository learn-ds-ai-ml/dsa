"""Dynamic List implementation in Python."""

from typing import cast


class DynamicList[T]:
    """Dynamic List."""

    def __init__(self) -> None:
        """Intialize the list."""
        self.size = 0
        self.capacity = 2
        self.array: list[T | None] = [None] * self.capacity

    def append(self, value: T) -> None:
        """Append the data to the list"""
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        self.array[self.size] = value
        self.size += 1

    def _resize(self, new_capacity: int) -> None:
        """Resize the array if its capacity is full.

        Args:
            new_capacity(int): new capacity of array
        """
        new_array: list[T | None] = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def insert(self, index: int, value: T) -> None:
        """Insert Value at an index.

        Args:
            index(int): index of insertion (zero based)
            value(T): Value to be inserted
        """
        if index < 0 or index > self.size:
            raise IndexError("Index out of range.")

        if self.size == self.capacity:
            self._resize(self.capacity * 2)

        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.size += self.size

    def delete(self, index: int) -> T:
        """Delete the value at particular index.

        Args:
            index(int): index of the array
        Returns:
            (T): deleted value
        """
        if index < 0 or index >= self.size:
            raise IndexError("index out of range.")

        value = cast(T, self.array[index])

        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]

        self.array[self.size - 1] = None
        self.size -= 1

        if self.capacity > 2 and self.size <= self.capacity // 4:
            self._resize(self.capacity // 2)

        return value


dl = DynamicList[int]()

dl.append(1)
print(dl.capacity)
print(dl.size)
print(dl.array)
print("---------")
dl.append(2)
print(dl.capacity)
print(dl.size)
print(dl.array)
print("---------")
dl.append(3)
print(dl.capacity)
print(dl.size)
print(dl.array)
print("---------")
dl.append(4)
print(dl.capacity)
print(dl.size)
print(dl.array)
print("---------")
dl.append(5)
print(dl.capacity)
print(dl.size)
print(dl.array)
print("---------")
dl.delete(4)
print(dl.capacity)
print(dl.size)
print(dl.array)
print("---------")
dl.delete(3)
print(dl.capacity)
print(dl.size)
print(dl.array)
print("---------")
dl.delete(2)
print(dl.capacity)
print(dl.size)
print(dl.array)
