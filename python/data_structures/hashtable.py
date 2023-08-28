class Hashtable:
    """
        Put docstring here
    """

    def __init__(self, size=100):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
        return sum(ord(char) for char in key) % self.size

    def set(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = []
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        if self.table[index] is None:
            return None
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def has(self, key):
        index = self._hash(key)
        if self.table[index] is None:
            return False
        for pair in self.table[index]:
            if pair[0] == key:
                return True
        return False

    def keys(self):
        key_list = []
        for entry in self.table:
            if entry:
                for pair in entry:
                    key_list.append(pair[0])
        return key_list

    def hash(self, key):
        return self._hash(key)
