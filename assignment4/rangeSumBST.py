# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        stk, sum = [root], 0
        while stk:
            node = stk.pop()
            if node:
                if node.val > low:
                    stk.append(node.left)    
                if node.val < high:
                    stk.append(node.right)
                if low <= node.val <= high:
                    sum += node.val    
        return sum