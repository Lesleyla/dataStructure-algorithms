# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        output = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            output.append(node.val)
            dfs(node.right)
        dfs(root)
        for i in range(1, len(output)):
            if output[i] <= output[i-1]:
                return False
        return True