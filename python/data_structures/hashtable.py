class Hashtable:
    """
        Put docstring here
    """

    def __init__(self, size=100):
        self.size = size
        self._buckets = [None] * self.size

    def _hash(self, key):
        return sum(ord(char) for char in key) % self.size

    def set(self, key, value):
        index = self._hash(key)
        if self._buckets[index] is None:
            self._buckets[index] = []
        for pair in self._buckets[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self._buckets[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        if self._buckets[index] is None:
            return None
        for pair in self._buckets[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def has(self, key):
        index = self._hash(key)
        if self._buckets[index] is None:
            return False
        for pair in self._buckets[index]:
            if pair[0] == key:
                return True
        return False

    def keys(self):
        key_list = []
        for entry in self._buckets:
            if entry:
                for pair in entry:
                    key_list.append(pair[0])
        return key_list

    def hash(self, key):
        return self._hash(key)

    def display(self):
        return [[pair for pair in bucket] if bucket else [] for bucket in self._buckets]

