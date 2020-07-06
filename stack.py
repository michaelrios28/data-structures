from linked_list import SinglyLinkedList


class Stack:
    def __init__(self):
        self.items = SinglyLinkedList()

    def __repr__(self):

        return str(self.items.toList())

    def push(self, item):
        self.items.addFirst(item)

    def pop(self):
        if self.items.isEmpty():
            return None

        top = self.items.getFirst()
        self.items.delFirst()
        return top

    def peek(self):
        if self.items.isEmpty():
            return None
        return self.items.getFirst()

    def isEmpty(self):
        return self.items.isEmpty()
