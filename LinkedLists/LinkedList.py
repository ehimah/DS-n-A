class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = Node(None)

    def append(self, value):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode
        return newNode

    def prepend(self, value):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        return newNode

    def reverseIterative(self):
        prev, curr, nxt = None, self.head, None

        while curr:
            nxt = curr.next
            curr.next = prev
            curr = nxt
            prev = curr

        self.head = prev
        return prev

    #[3,4,5,6,7,8]
    #[8,7]
    def reverseRecursive(self):
        def helper(node: Node):
            if not node.next:
                return node
            newhead = helper(node.next)
            restTail = node.next
            restTail.next = node
            newhead.next = node
            node.next = None
            return newhead

        return helper(self.head)