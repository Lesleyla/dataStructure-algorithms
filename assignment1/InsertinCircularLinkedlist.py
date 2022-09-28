"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal, None)
            head.next = head
            return head
        if not head.next:
            head.next = Node(insertVal, head)
            return head
        # if current val < next node's val: 
        # Insert only if current val <= insertVal <= next node's val
        # if current val > next node's val:
        # Insert only if current val <= insertVal or insertVal <= next node's val
        # if you reach back to head i.e. all nodes had same value
        # so insert after head
        tmp = head
        while True:
            if tmp.val < tmp.next.val:
                if tmp.val <= insertVal <= tmp.next.val:
                    tmp.next = Node(insertVal, tmp.next)
                    return head
            if tmp.val > tmp.next.val:
                if insertVal >= tmp.val or insertVal <= tmp.next.val:
                    tmp.next = Node(insertVal, tmp.next)
                    return head
            tmp = tmp.next # When all elements had same value
            if tmp == head:
                tmp.next = Node(insertVal, tmp.next)
                return head