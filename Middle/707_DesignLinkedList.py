"""
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next.
val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate
the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.
"""

class Node:
    def __init__(self):
        self.value = None
        self.next = None
        self.prev = None

class MyLinkedList:
    def __str__(self):
        values = []
        pointer = self.head
        while pointer is not None:
            values.append(pointer.value)
            pointer = pointer.next
        return str(values)

    def __init__(self):
        self.head = Node()

    def get(self, index: int) -> int:
        pointer = self.head
        for i in range(index):
            if pointer.next is not None:
                pointer = pointer.next
            else:
                return -1
        return pointer.value

    def addAtHead(self, val: int) -> None:
        if self.head.value is None:
            self.head.value = val
        else:
            new = Node()
            new.value = val
            self.head.prev = new
            new.next = self.head
            self.head = new

    def addAtTail(self, val: int) -> None:
        if self.head.value is None:
            return self.addAtHead(val)

        pointer = self.head
        while pointer.next is not None:
            pointer = pointer.next
        new = Node()
        new.value = val
        new.prev = pointer
        pointer.next = new

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            return self.addAtHead(val)

        length = 0
        pointer = self.head
        while pointer is not None:
            pointer = pointer.next
            length += 1

        if index == length:
            self.addAtTail(val)
        else:
            pointer = self.head
            for i in range(index):
                if pointer.next is not None:
                    pointer = pointer.next
                else:
                    return

            new = Node()
            new.value = val
            new.next = pointer
            pointer.prev.next = new
            new.prev = pointer.prev
            pointer.prev = new

    def deleteAtIndex(self, index: int) -> None:
        pointer = self.head
        for i in range(index):
            if pointer.next is not None:
                pointer = pointer.next
            else:
                return
        if pointer.prev is not None:
            pointer.prev.next = pointer.next
        else:
            pointer.prev = None
            self.head = pointer.next

        if pointer.next is not None:
            pointer.next.prev = pointer.prev
        else:
            pointer.next = None




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# ["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
# [[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]
# [null,null,null,null,null,null,null,null,4,null,null,null]

my_list = MyLinkedList()
my_list.addAtHead(7)
my_list.addAtHead(2)
my_list.addAtHead(1)
print(my_list)
my_list.addAtIndex(3, 0)
print(my_list)
my_list.deleteAtIndex(2)
print(my_list)
my_list.addAtHead(6)
my_list.addAtTail(4)
print(my_list)
print(my_list.get(4))
my_list.addAtHead(4)
my_list.addAtIndex(0, 1)
my_list.addAtHead(6)
print(my_list)
my_list.deleteAtIndex(0)
print(my_list)
print(my_list.get(4))

