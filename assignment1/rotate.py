# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        
        #get the number of nodes, and record the last node
        last = head
        cnt = 1
        while last.next:
            cnt += 1
            last = last.next
        k = k % cnt
        
        last.next = head
        tmpNode = head
        for _ in range(cnt - k - 1):
            tmpNode = tmpNode.next

        res = tmpNode.next
        tmpNode.next = None
        
        return res