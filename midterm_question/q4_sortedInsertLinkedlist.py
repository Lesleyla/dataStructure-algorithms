class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertDataInSortedLinkedList(self, head: ListNode, insertData: int) -> ListNode:
        dummy_node = ListNode(-1)
        #value of dummy node depends on the constraints of nodes value of input linked list
        #value of dummy node must < node value of linked list
        #use dummy node, prevent the situation that insertdata is less than the val of head
        dummy_node.next = head
        pre = dummy_node
        cur = pre.next
        flg = False
        while cur:
            if cur.val >= insertData:
                pre.next = ListNode(insertData)
                pre.next.next = cur
                flg = True#the data hax been inserted
                break
            cur = cur.next
            pre = pre.next
        #after loop, check if the data has been insert: if not inserted yet, put the data into the tail
        if flg == False:
            pre.next = ListNode(insertData)
        return dummy_node.next