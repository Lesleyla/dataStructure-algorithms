# Definition for a binary tree node.
from collections import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        queue = [root]
        
        rev = 0
        while queue:
            next_nodes, level_vals = [], []
            for node in queue:
                if not node:
                    continue
                next_nodes.append(node.left)
                next_nodes.append(node.right)
                level_vals.append(node.val)
            level_vals = level_vals if not rev else level_vals[::-1]
            if level_vals:
                res.append(level_vals)
            rev = ~rev
            queue = next_nodes
        return res