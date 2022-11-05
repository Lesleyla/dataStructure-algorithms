# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.preorder = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.preorder.append(root.val)
            dfs(root.right)
        dfs(root)
        self.idx = -1
        
    def next(self) -> int:
        self.idx += 1
        return self.preorder[self.idx]

    def hasNext(self) -> bool:
        l = len(self.preorder)
        return True if self.idx < l-1 else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()