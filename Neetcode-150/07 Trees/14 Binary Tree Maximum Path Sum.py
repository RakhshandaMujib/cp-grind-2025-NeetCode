# Title: Binary Tree Maximum Path Sum
# Link: https://neetcode.io/problems/binary-tree-diameter
# Difficulty: Hard 
# Tags: Trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # For a single node the maxSum would be the root value
        self.maxSum = root.val

        # Recursive funvtion
        def getSum(node):

            # Edge case
            if node == None:
                return 0

            # Get the sum of the children nodes
            left_sum = getSum(node.left)
            right_sum = getSum(node.right)

            # 4 candidate paths are available for computing the maxSum
            # maxSum so far, only the node (in case both the children are -ve),
            # node + one child node (in case one of the children is -ve)
            self.maxSum = max(self.maxSum, \
                              node.val, \
                              node.val + left_sum, \
                              node.val + right_sum, \
                              node.val + left_sum + right_sum)

            # Return will only extend to one child not both to maintain the 
            # valid path
            return max(node.val, node.val + left_sum, node.val + right_sum)
        
        # Start recursion at the root
        getSum(root)

        # Return the max sum path
        return self.maxSum