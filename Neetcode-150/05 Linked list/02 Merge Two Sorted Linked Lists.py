# Title: Merge Two Sorted Linked Lists
# Link: https://neetcode.io/problems/merge-two-sorted-linked-lists
# Difficulty: Easy 
# Tags: Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Initialize temporary pointers to the lists
        t1, t2 = list1, list2

        # Get a dummy head
        dummy = ListNode()
        # Iterator current pointer to stitch the merged lists
        curr = dummy

        
        # Pick the smaller number and make the curr
        # node point to it.
        while t1 and t2:
            if t1.val <= t2.val:
                curr.next = t1
                # Iterate t1
                t1 = t1.next
            else:
                curr.next = t2
                # Iterate t2
                t2 = t2.next
            
            # Iterate curr
            curr = curr.next
        
        # Attach the ends of the bigger list
        if t1:
            curr.next = t1
        elif t2:
            curr.next = t2

        # Return the dummy head
        return dummy.next