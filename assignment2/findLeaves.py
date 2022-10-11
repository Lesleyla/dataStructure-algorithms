#find leaves
# Definition for a binary tree node.
from collections import List, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        def order(root, dic):
            if not root:
                return 0
            left = order(root.left, dic)
            right = order(root.right, dic)
            level = max(left, right) + 1
            dic[level].append(root.val)
            return level
        dic = defaultdict(list)
        order(root, dic)
        idx = sorted(dic)
        return [dic[i] for i in idx]