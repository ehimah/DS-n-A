from .DoubleLinkedList import DoublyLinkedList
from .DoubleLinkedList import Node


class LRUCache:
    def __init__(self, size: int) -> None:
        self.dll = DoublyLinkedList()
        self.items = dict()
        self.size = size

    def get(self, key):
        # if in cache then move to front
        if key in self.items:
            node = self.items[key]
            print('to promote => ', node.val)
            self.dll.promoteToHead(node)
        else:
            # add to cache
            if self.isFull():
                removed = self.dll.remove(self.dll.tail)
                del self.items[removed.val]
            node = self.dll.prepend(key)
            self.items[key] = node
        return

    def isFull(self) -> bool:
        return len(self.items) == self.size

    def print(self):
        curr = self.dll.head
        result = []
        while curr:
            result.append(curr.val)
            curr = curr.next
        print(result)