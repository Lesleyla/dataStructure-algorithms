# Definition for a binary tree node.
from collections import deque, defaultdict, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        cols = defaultdict(list)
        queue = deque([(root, 0)])
        while queue:
            node, i = queue.popleft()
            cols[i].append(node.val)
            if node.left:
                queue.append((node.left, i-1))
            if node.right:
                queue.append((node.right, i+1))
        idxs = sorted(cols)
        return [cols[i] for i in idxs]