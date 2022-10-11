# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(l, r):
            if l and r:
                if l.val != r.val: return False
                elif (not check(l.left, r.right)) or (not check(r.left, l.right)): return False
                else: return True
            elif l or r:
                return False
            else:
                return True
        return check(root, root)