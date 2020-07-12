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
        index = self.__hash(key)
        index_linked_list = self.array[index]

        # check to see if key already exists
        if len(index_linked_list):
            # search through linked list
            for node in index_linked_list:
                if node[0] == key:
                    node[1] = value
        else:
            # handle collisions w/ chaining
            index_linked_list.append(list([key, value]))

    def get(self, key):
        index = self.__hash(key)
        index_linked_list = self.array[index]

        for k, v in index_linked_list:
            if k == key:
                return v

        raise KeyError(key)  # key wasn't found

    def remove(self, key):
        index = self.__hash(key)
        index_linked_list = self.array[index]

        found = False
        for node in index_linked_list:
            if node[0] == key:
                found = True
                break
        if found:
            index_linked_list.remove(node)
        else:
            raise KeyError(key)  # key wasn't found


if __name__ == "__main__":

    ht = HashTable(size=5)
    print('array', ht.array)
    ht.put('b', 4)
    print('array', ht.array)
    print('get', ht.get('b'))
    ht.put('b', 6)
    ht.put('b', 7)
    ht.put('a', 117)
    ht.put(None, 117)
    print('array', ht.array)
    print('get', ht.get('b'))
    print('remove b', ht.remove('c'))
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
