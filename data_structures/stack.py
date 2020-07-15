from linked_list import SinglyLinkedList


class Stack:
    def __init__(self):
        self.items = SinglyLinkedList()

    def __repr__(self):
        return str(self.items.toList())

    # O(1)
    def push(self, item):
        self.items.addFirst(item)

    # O(1)
    def pop(self):
        if self.items.isEmpty():
            return None

        top = self.items.getFirst()
        self.items.delFirst()
        return top

    # O(1)
    def peek(self):
        if self.items.isEmpty():
            return None
        return self.items.getFirst()

    # O(1)
    def isEmpty(self):
        return self.items.isEmpty()
