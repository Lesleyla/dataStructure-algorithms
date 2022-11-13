from collections import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def BSTPrintValueInRange(self, root: TreeNode, left: int, right: int) -> List[int]:
        res = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if left <= node.val <= right:
                res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res