# Title: Diameter of Binary Tree
# Link: https://neetcode.io/problems/binary-tree-diameter
# Difficulty: Easy 
# Tags: Trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # Track the diameter
        self.diam = 0

        # Helper method to do the recursion
        def getHeight(node):

            # Base condition
            if not node:
                return 0

            # Get the left and the right height which is going to 
            # contribute to the diameter
            left_ht = getHeight(node.left)
            right_ht = getHeight(node.right)

            # Diameter for a single node is the sum of the left
            # and right nodes' heights.
            # Update it.
            self.diam = max(self.diam, left_ht + right_ht)

            # Return the depth
            return 1 + max(left_ht, right_ht)

        # Call the recursive method
        getHeight(root)

        return self.diam