# Title: Balanced Binary Tree
# Link: https://neetcode.io/problems/balanced-binary-tree
# Difficulty: Easy 
# Tags: Trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def getDepth(node) -> int:

            if not node:
                return 0
            
            left_ht = getDepth(node.left)
            if left_ht == -1:
                return -1 # Early exit

            right_ht = getDepth(node.right)
            if right_ht == -1:
                return -1 # Early exit

            # If the difference between the depths is > 1, 
            # the tree isn't balanced
            if abs(left_ht - right_ht) > 1:
                return -1
            
            # Return the depth
            return 1 + max(left_ht, right_ht)
        
        return getDepth(root) != -1