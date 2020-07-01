

class SinglyLinkedList:
    class __Node:
        def __init__(self, val=0):
            self.val = val
            self.next = None

    def __init__(self):
        self.__head = None
        self.__tail = None  # keep track of __tail to make it more efficient
        self.__size = 0

    def __repr__(self):
        string = ''
        current = self.__head

        while current:
            string += f"{current.val} -> "
            current = current.next
        return string[0:-3]

    def isEmpty(self):
        return self.__head == None

    # O(1)
    def addFirst(self, val):
        n = SinglyLinkedList.__Node(val)

        if self.isEmpty():
            self.__head = self.__tail = n
        else:
            n.next = self.__head
            self.__head = n

        self.__size += 1

    # O(1)
    def addLast(self, val):
        n = SinglyLinkedList.__Node(val)

        if self.isEmpty():
            self.__head = self.__tail = n
        else:
            self.__tail.next = n
            self.__tail = n

        self.__size += 1

    # O(1)
    def delFirst(self):
        if self.isEmpty():
            raise Exception('No such element. Empty list.')

        # contains one node
        if self.__head == self.__tail:
            self.__head = self.__tail = None
            self.__size -= 1
            return

        first = self.__head
        self.__head = first.next
        first.next = None

        self.__size -= 1

    # O(n)
    def delLast(self):
        if self.isEmpty():
            raise Exception('No such element. Empty list.')

        # contains one node
        if self.__head == self.__tail:
            self.__head = self.__tail = None
            self.__size -= 1
            return

        # get second to last node
        current = self.__head
        while current.next.next:
            current = current.next

        self.__tail = current
        current.next.val = None
        current.next = None

        self.__size -= 1

    # O(n)

    def contains(self, val):
        current = self.__head
        while current:
            if (current.val == val):
                return True
            current = current.next
        return False

    # O(n)
    def indexOf(self, val):
        index = 0
        current = self.__head
        while current:
            if (current.val == val):
                return index
            index += 1
            current = current.next
        return -1

    # O(n)
    def size(self):
        return self.__size


s = SinglyLinkedList()
s.addFirst(3)
s.addFirst(2)
print('size', s.size())
print(s)
print('index of 3', s.indexOf(3))
print('index of 2', s.indexOf(2))
s.delLast()
print('size', s.size())
# s.delFirst()
print(s)
