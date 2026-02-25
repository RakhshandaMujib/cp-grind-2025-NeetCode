# Title: Same Binary Tree
# Link: https://neetcode.io/problems/same-binary-tree
# Difficulty: Easy 
# Tags: Trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

    	# Case 1:
    	# If both the nodes don't exist -> Both trees match at this node
        if not p and not q:
            return True
            
        # Case 2: 
        # If one node exists and the other doesn't -> Mismatch
        # Short-circuit.
        if not p or not q:
            return False
            
        # Case 3:
        # If both nodes exist but the values aren't the same -> Mismatch
        # Short-circuit.
        if p.val != q.val:
            return False
            
        # Case 4: 
        # Both nodes exist AND the values match
        # Now, recurse on the left children AND the right children
        return self.isSameTree(p.left, q.left) and \
        	   self.isSameTree(p.right, q.right)