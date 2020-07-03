

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
        else:
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
        else:
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

    # O(1)
    def size(self):
        return self.__size

    # O(n)
    def toList(self):
        # set init size to reduce having to recreate array
        converted = [0] * self.__size
        index = 0
        current = self.__head

        while current:
            converted[index] = current.val
            index += 1
            current = current.next
        return converted

    # O(n)
    def reverse(self):
        if self.isEmpty():
            raise Exception('No such element. Empty list.')

        if self.__head == self.__tail:
            return

        # reverse the linked list in place
        current = self.__head.next
        prev = self.__head

        # swap head and tail pointers
        temp = self.__head
        self.__head = self.__tail
        self.__tail = temp
        self.__tail.next = None

        while current:
            if not current.next:
                current.next = prev
                return

            nxt = current.next
            current.next = prev
            prev = current
            current = nxt


s = SinglyLinkedList()
# test zero items
# test one item in list
s.addLast(1)
s.addLast(2)
s.addLast(3)

print(s)
s.reverse()
print('reversed', s)
print('converted', s.toList())
# test multiple items in list
