class Node:
    def __init__(self, value) -> None:
        self.prev = None
        self.next = None
        self.val = value


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def prepend(self, value):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            curr = self.head
            newNode.next = curr
            curr.prev = newNode
            self.head = newNode
        return newNode

    def append(self, value) -> Node:
        newNode = Node(value)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        return newNode

    def remove(self, node: Node) -> Node:
        if node == self.head:
            print('remove head', node.val)
            self.head = self.head.next
        elif node == self.tail:
            print('remove tail', node.val)
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            tmp = node
            print('remove middle', node.val)
            node.prev.next = tmp.next
            node.next.prev = tmp.prev
        return node

    def promoteToHead(self, node: Node):
        if node == self.head:
            return
        elif node.next:
            node.next.prev = node.prev

        node.prev.next = node.next
        self.head.prev = node
        node.next = self.head
        self.head = node
