# Title: Invert Binary Tree
# Link: https://neetcode.io/problems/invert-a-binary-tree
# Difficulty: Easy 
# Tags: Trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    	if not root:
    		return None

    	# Exhange the children nodes (not just the values, the actual nodes)
    	root.left, root.right = root.right, root.left

    	# Invert the children nodes
    	self.invertTree(root.left)
    	self.invertTree(root.right)

    	return root