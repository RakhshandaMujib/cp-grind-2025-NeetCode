# Title: Reorder Linked List
# Link: https://neetcode.io/problems/reorder-linked-list
# Difficulty: Medium 
# Tags: Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        1. Find the mid -- use slow-fast pointer
        2. Reverse the 2nd half of the LL to store all
           the previous pointers (that would otherwise
           get lost).
        3. Merge both the lists to one -- 
           left->right.next->left.next...
        '''
        # If empty or single element in the list
        if not head or not head.next:
            return

        # Step 1:
        mid = ListNode()
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # Slow pointer will return the mid of the list
        mid = slow

        # Step 2:
        prev = None
        # mid belongs to the first half.
        # We start reversing from (mid+1).
        # Cutting at mid:     mid -> None
        # Original second:    (mid+1) -> (mid+2) -> ... -> n -> None
        # After reversal:      n -> ... -> (mid+2) -> (mid+1) -> None
        curr = nxt = mid.next
        mid.next = None # To avoid cycles

        # Reversal begins:
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # Step 3:
        second = prev # Tail of the second list
        first = head # Head of the first list

        while second:
            # Temporary pointers
            first_right = first.next # The node right from the head
            second_left = second.next # The node left to the tail

            #Interleave the nodes
            first.next = second # Eg: 0 -> n
            second.next = first_right # Eg: n-1 -> 1

            # Update the head of first and tail of second lists
            first = first_right # Eg: From 0 to 1
            second = second_left # Eg: From n to n-1