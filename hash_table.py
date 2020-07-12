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
        self.array = [deque() for _ in range(size)]
        print(f"Hash Table initialized w/ size of {self.__size}")

    def __hash(self, key):
        hashed_key_hex_string = hashlib.sha256(str(key).encode()).hexdigest()
        hashed_key_int = int(hashed_key_hex_string, 16)
        return hashed_key_int % self.__size

    def put(self, key, value):
        print("test hash", self.__hash(key))
        index = self.__hash(key)
        self.array[index].append(tuple([key, value]))

    def get(self, key):
        # get index
        index = self.__hash(key)
        for k, v in self.array[index]:
            if k == key:
                return v


if __name__ == "__main__":

    ht = HashTable(size=5)
    print('array', ht.array)
    ht.put('a', 2)
    ht.put('b', 4)
    ht.put('c', 6)
    ht.put('lastKey', 6)

    print('get', ht.get('a'))
    print('array', ht.array)

    # find the first non-repeating character in:
    # a green apple

    # approach
    # iterate through the string O(n)
    # store the chars(k) and occurances(v) in a dictionary
    # iterate through the string (since no order) and find first char w/ 1 occurance

    def getFirstNonRepeatingChar(strng):
        char_dict = dict()
        for char in strng:
            if char_dict.get(char):
                char_dict[char] += 1
            else:
                char_dict[char] = 1

        for char in strng:
            if char_dict.get(char) == 1:
                return char

    def getFirstRepeatingChar(strng):
        char_set = set()
        for char in strng:
            if char in char_set:
                return char
            else:
                char_set.add(char)
