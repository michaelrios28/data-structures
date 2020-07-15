# hash table
# put(k, v)
# get(k): v
# remove(k)
# Collisions are handled by chaining

from collections import deque
import hashlib


class HashTable():
    def __init__(self, *, size):
        self._size = size
        # self._array = [deque() for _ in range(size)]
        self._array = [None] * size
        print(f"Hash Table initialized w/ size of {self._size}")

    def _hash(self, key):
        hashed_key_hex_string = hashlib.sha256(str(key).encode()).hexdigest()
        hashed_key_int = int(hashed_key_hex_string, 16)
        return hashed_key_int % self._size

    def _get_node(self, key):
        index = self._hash(key)
        bucket = self._array[index]
        if bucket:
            for node in bucket:
                k = node[0]
                if k == key:
                    return node

        return None

    def _get_bucket(self, key):
        index = self._hash(key)
        return self._array[index]

    def _get_or_create_bucket(self, key):
        index = self._hash(key)
        bucket = self._array[index]
        if not bucket:
            self._array[index] = deque()
        return self._array[index]

    def put(self, key, value):
        node = self._get_node(key)
        if node:
            node[1] = value
            return

        bucket = self._get_or_create_bucket(key)
        bucket.append(list([key, value]))

    def get(self, key):
        node = self._get_node(key)
        if node:
            value = node[1]
            return value
        else:
            raise KeyError(key)  # key wasn't found

    def remove(self, key):
        node = self._get_node(key)
        if node:
            self._get_bucket(key).remove(node)
        else:
            raise KeyError(key)  # key wasn't found


if __name__ == "__main__":

    ht = HashTable(size=5)
    print('testing put method')
    ht.put('b', 4)
    print('_array', ht._array)

    print('testing get method')
    print('getting b ->', ht.get('b'))

    print('testing put method overwrite')
    ht.put('b', 6)
    print('_array', ht._array)

    print('testing remove method')
    print('removing b', ht.remove('b'))
    print('_array', ht._array)

    print('testing accessing non-existent key')
    print('getting b ->', ht.get('c'))
