# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #find whether left subtree or right subtree has p or q
        #if one in node.left subtree and another one in node.right subtree: node is the answer
        #if p ,q in the same one side tree, keep find this side tree:make root change to root.side
        #if subtree contains neigher:return None
        
        #corner case:
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right:
            return
        elif not left:
            return right
        elif not right:
            return left
        else:
            return root