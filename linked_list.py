

class SinglyLinkedList:
    class __Node:
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        self.head = None

    def __repr__(self):
        string = ''
        current = self.head

        while current.next:
            string += f"{current.val} -> "
            current = current.next
        string += str(current.val)
        return string

    # O(1)
    def addFirst(self, val):
        n = SinglyLinkedList.__Node(val)
        n.next = self.head
        self.head = n

    # O(n)
    def addLast(self, val):
        current = self.head
        while current.next:
            current = current.next
        current.next = SinglyLinkedList.__Node(val)

    # O(1)
    def delFirst(self):
        head = self.head
        self.head = head.next
        head = None

    # O(n)
    def delLast(self):
        current = self.head
        while current.next.next:
            current = current.next
        current.next.val = None
        current.next = None

    # O(n)
    def contains(self, val):
        current = self.head
        while current:
            if (current.val == val):
                return True
            current = current.next
        return False

    # O(n)
    def indexOf(self, val):
        index = 0
        current = self.head
        while current:
            if (current.val == val):
                return index
            index += 1
            current = current.next
        return -1


s = SinglyLinkedList()
s.addFirst(2)
s.addFirst(4)
s.addFirst(6)
s.addLast(10)
s.addFirst(69)
s.addLast(100)
s.addLast(101)
s.addFirst(0)


print('head', s.head)
s.delFirst()
print(s)
s.delLast()
print(s)
print('indexOf?', s.indexOf(69))
print('indexOf?', s.indexOf(200))
