class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        self.size = self.size + n
        if self.size > self.capacity:
            raise ValueError("Adding that many cookies would exceed the jar's capacity")
        return self.size

    def withdraw(self, n):
        self.size = self.size - n
        if self.size < 0:
            raise ValueError("Cannot remove that many cookies, there aren't that many")
        return self.size

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0 or size > self.capacity:
            raise ValueError("Invalid size, size is outside of the capacity's limits")
        self._size = size


jar = Jar()

jar.deposit(9)
jar.deposit(2)

jar.withdraw(5)

print(jar.size)
print(jar)
