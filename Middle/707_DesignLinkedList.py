"""
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next.
val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate
the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.
"""
# singly linked list
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
        if pointer.value is not None:
            return pointer.value
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        if self.head.value is None:
            self.head.value = val
        else:
            new = Node()
            new.value = val
            new.next = self.head
            self.head = new

    def addAtTail(self, val: int) -> None:
        if self.head.value is None:
            return self.addAtHead(val)
        else:
            pointer = self.head
            while pointer.next is not None:
                pointer = pointer.next

            new = Node()
            new.value = val
            pointer.next = new

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            return self.addAtHead(val)
        # find list len
        length = 0
        pointer = self.head
        while pointer is not None and pointer.value is not None:
            pointer = pointer.next
            length += 1

        if index == length:
            self.addAtTail(val)
        elif index < length:
            pointer = self.head
            for i in range(index-1):
                if pointer.next is not None:
                    pointer = pointer.next
                else:
                    return
            new = Node()
            new.value = val
            next_pointer = pointer.next
            new.next = next_pointer
            pointer.next = new

    def deleteAtIndex(self, index: int) -> None:

        if index == 0:
            if self.head.next is not None:
                self.head = self.head.next
            else:
                self.head.value = None
        else:
            pointer = self.head
            for i in range(index-1):
                if pointer.next is not None:
                    pointer = pointer.next
                else:
                    return
            if pointer.next is not None:
                pointer.next = pointer.next.next




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# ["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
# [[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]
# [null,null,null,null,null,null,null,null,4,null,null,null]

my_list = MyLinkedList()

print(my_list)
my_list.addAtHead(1)
my_list.addAtHead(2)
print(my_list.addAtIndex(1, 0))
print(my_list)
print(my_list.get(0))



