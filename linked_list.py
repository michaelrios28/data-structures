

class SinglyLinkedList:
    class __Node:
        def __init__(self, val=0):
            self.val = val
            self.next = None

    def __init__(self):
        self.__head = None
        self.__tail = None  # keep track of __tail to make it more efficient

    def __repr__(self):
        string = ''
        current = self.__head

        while current.next:
            string += f"{current.val} -> "
            current = current.next
        string += str(current.val)
        return string

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

    # O(1)
    def addLast(self, val):
        n = SinglyLinkedList.__Node(val)

        if self.isEmpty():
            self.__head = self.__tail = n
        else:
            self.__tail.next = n
            self.__tail = n

    # O(1)
    def delFirst(self):
        __head = self.__head
        self.__head = __head.next
        __head = None

    # O(n)
    def delLast(self):
        current = self.__head
        while current.next.next:
            current = current.next

        # second to last node
        self.__tail = current
        current.next.val = None
        current.next = None

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


s = SinglyLinkedList()
s.addFirst(3)
s.addFirst(2)
s.addFirst(1)
s.addLast(69)
s.addLast(100)
s.addLast(101)
s.addFirst(1)
print(s)
