# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        #queue for keeping track
        queue = deque([(0, root)])
        width = 0
        while queue:
            # nodes list to store indexes of all nodes at a level
            nodes = []
            for _ in range(len(queue)):
                idx, node = queue.popleft()
                nodes.append(idx)
                if node.left:
                    queue.append((2*idx+1 , node.left))
                if node.right:
                    queue.append((2*idx+2 , node.right))
            # max of ans or (right-most index - left-most index + 1) for a level
            width = max(width, max(nodes)-min(nodes)+1)
        return width