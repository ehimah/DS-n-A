class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def fromList(list):
        l1 = LinkedList()
        for i in list:
            l1.append(i)
        return l1

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

    # [3,4,5,6,7,8]
    # [8,7]
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

    def mergeSorted(l1: Node, l2: Node) -> Node:
        head, p1, p2 = Node(0), l1, l2
        curr = head

        while p1 and p2:
            if p1.value < p2.value:
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next
            curr = curr.next

        while p1:
            curr.next = p1
            p1 = p1.next
            curr = curr.next

        while p2:
            curr.next = p2
            p2 = p2.next
            curr = curr.next

        return head.next
