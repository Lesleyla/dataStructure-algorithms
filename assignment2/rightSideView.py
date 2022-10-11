# Definition for a binary tree node.
from collections import List, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        #right side view -> level order
        if not root:
            return []
        res = []
        stack = deque([root])
        while stack:
            for _ in range(len(stack)):
                tmp = []
                node = stack.popleft()
                if node:
                    tmp.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            if tmp:
                res.append(tmp[-1])
        return res