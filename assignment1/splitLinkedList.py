# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        size = self.get_size(head)
        min_len, one_more = divmod(size, k)
        res = []
        current = ListNode()
        current.next = head
        for i in range(k):
            ans = current
            for _ in range(min_len + int(i < one_more)):
                current = current.next
            res.append(ans.next)
            ans.next = None
        return res

    def get_size(self, head: ListNode) -> int:
        size = 0
        while head is not None:
            size += 1
            head = head.next
        return size