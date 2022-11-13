# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, parent: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class Solution:
    #populate the parent pointers in each node
    def connectParent(self, root: 'Node') -> 'Node':
        if not root:
            return None
        self.con2(root, root.left)
        self.con2(root, root.right)
        return root
    def con2(self,parent_node, child_node):
        if not child_node:
            return
        child_node.parent = parent_node
        self.con2(child_node, child_node.left)
        self.con2(child_node, child_node.right)