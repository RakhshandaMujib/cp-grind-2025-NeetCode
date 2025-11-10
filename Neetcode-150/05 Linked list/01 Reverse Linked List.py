# Title: Reverse Linked List
# Link: https://neetcode.io/problems/reverse-a-linked-list
# Difficulty: Easy 
# Tags: Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Initialize the previous and current pointer
        prev, curr = None, head
        
        while curr:
        	# Update the next pointer
            nxt = curr.next
            # Break the connection with next node and make the current node
            # point to the previous node
            curr.next = prev
            # Update the previous node to the current node
            prev = curr
            # Update the current node to the next node
            curr = nxt
        
        # Current node is Null when reaching the end
        # Previous node holds the last node
        return prev