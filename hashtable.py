from multipledispatch import dispatch


class HtNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self, size = 20):
        self.size = size
        self.table = []
        for i in range(size):
            self.table.append([])

    def _hash(self, key):
        return hash(key) % self.size

    @dispatch(HtNode)
    def add(self, node):
        key = node.key
        value = node

        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    @dispatch(int, HtNode)
    def add(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])


    def search(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        raise KeyError(key)

    def remove(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return
        raise KeyError(key)