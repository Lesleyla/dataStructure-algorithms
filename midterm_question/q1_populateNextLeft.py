# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, nextleft: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.nextleft = nextleft

class Solution:
    #this funtion is to populate the nextleft pointers in each node
    def connectNextLeft(self, root: 'Node') -> 'Node':
        if not root:
            return None
        self.con2(root.left,root.right)
        return root
    def con2(self,node1,node2):
        if not node1 or not node2:
            return
        node2.nextleft = node1
        self.con2(node1.left,node1.right)
        self.con2(node2.left,node2.right)
        self.con2(node1.right,node2.left)