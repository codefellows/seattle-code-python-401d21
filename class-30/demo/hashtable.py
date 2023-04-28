class Hashtable:
    def __init__(self, size=1024):
        self._size = size
        self._buckets = size * [None]

    def set(self, key, value):
        # TODO: Hash the key
        pass

    def get(self, key):
        # TODO: Hash the key
        pass

    def has(self, keyy):
        # TODO: Hash the key
        pass

    def keys(self):
        pass

    # 'Roger'
    #      ^
    # Total = 82 + 111 + 103 + 101 + 114 = 510
    # 510 multiple by a prime number
    def hash(self, key):
        hash_total = 0
        for char in key:
            hash_total += ord(char)
        primed_number = hash_total * len(key) * 19
        index = primed_number % self._size
        return index
