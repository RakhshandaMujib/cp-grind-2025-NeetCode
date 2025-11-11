# Title: Linked List Cycle Detection
# Link: https://neetcode.io/problems/linked-list-cycle-detection
# Difficulty: Easy 
# Tags: Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # slow moves one step at a time
        # fast moves two steps at a time
        slow = fast = head

        # Keep looping if either fast exists or fast.next exists.
        while fast and fast.next:
            
            # Update the pointers
            slow = slow.next
            fast = fast.next.next

            # If the two pointers meet, cycle identified
            if slow == fast:
                return True

        # Cycle doesn't exist.
        return False
        