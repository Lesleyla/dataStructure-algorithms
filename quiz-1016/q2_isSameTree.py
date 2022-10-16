# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        #use recursion
        def isSameNode(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            return node1.val == node2.val and isSameNode(node1.left, node2.left) and isSameNode(node1.right, node2.right)
        
        return isSameNode(p, q)