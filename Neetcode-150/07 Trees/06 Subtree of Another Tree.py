# Title: Subtree of Another Tree
# Link: https://neetcode.io/problems/subtree-of-a-binary-tree
# Difficulty: Easy 
# Tags: Trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # If the sub root doesn't exist, it is a subtree
        if subRoot == None:
            return True
        
        # Base case for the outer recursion
        if root == None:
            return False

        # Helper method to recurse over the candidate subtree and the 
        # current subtree. Returns True if both are the same.
        def sameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return sameTree(p.left, q.left) and sameTree(p.right, q.right)

        # If the subtree doesn't match at the root
        if not sameTree(root, subRoot):

            # Recurse on the children
            return self.isSubtree(root.left, subRoot) or \
                   self.isSubtree(root.right, subRoot)

        # If the subtree matches at the root, return True
        return True