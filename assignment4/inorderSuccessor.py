# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        res = []#tree nodes stored here
        self.ret = None
        self.inOrder(root, res, p)
        return self.ret
        
    def inOrder(self, root, res, p):#recursion
        if root:
            self.inOrder(root.left, res, p)
            res.append(root)
            if len(res) > 1 and res[-2] == p:
                self.ret = res[-1]
                return 
            self.inOrder(root.right, res, p)