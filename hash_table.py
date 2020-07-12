# hash table
# put(k, v)
# get(k): v
# remove(k)
# Collisions are handled by chaining

from collections import deque
import hashlib


class HashTable():
    def __init__(self, *, size):
        self.__size = size
        # self.array = [deque() for _ in range(size)]
        self.array = [None] * size
        print(f"Hash Table initialized w/ size of {self.__size}")

    def __hash(self, key):
        hashed_key_hex_string = hashlib.sha256(str(key).encode()).hexdigest()
        hashed_key_int = int(hashed_key_hex_string, 16)
        return hashed_key_int % self.__size

    def __get_node(self, key):
        index = self.__hash(key)
        bucket = self.array[index]
        if bucket:
            for node in bucket:
                k = node[0]
                if k == key:
                    return node

        return None

    def __get_bucket(self, key):
        index = self.__hash(key)
        return self.array[index]

    def __get_or_create_bucket(self, key):
        index = self.__hash(key)
        bucket = self.array[index]
        if not bucket:
            self.array[index] = deque()
        return self.array[index]

    def put(self, key, value):
        node = self.__get_node(key)
        if node:
            node[1] = value
            return

        bucket = self.__get_or_create_bucket(key)
        bucket.append(list([key, value]))

    def get(self, key):
        node = self.__get_node(key)
        if node:
            value = node[1]
            return value
        else:
            raise KeyError(key)  # key wasn't found

    def remove(self, key):
        node = self.__get_node(key)
        if node:
            self.__get_bucket(key).remove(node)
        else:
            raise KeyError(key)  # key wasn't found


if __name__ == "__main__":

    ht = HashTable(size=5)
    print('testing put method')
    ht.put('b', 4)
    print('array', ht.array)

    print('testing get method')
    print('getting b ->', ht.get('b'))

    print('testing put method overwrite')
    ht.put('b', 6)
    print('array', ht.array)

    print('testing remove method')
    print('removing b', ht.remove('b'))
    print('array', ht.array)

    print('testing accessing non-existent key')
    print('getting b ->', ht.get('c'))
