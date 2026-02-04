# Title: Reverse Nodes in K-Group
# Link: https://neetcode.io/problems/reverse-nodes-in-k-group
# Difficulty: Hard 
# Tags: Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # Tracks the first traversal for updating the head
        first_reversal = True
        
        # Initialize the pointers
        curr = head
        temp_head = curr # Tracks the head of a segment
        temp_tail = None # Tracks the tail of a segment
        prev_tail = None # Stores the tail of the previous segment i.e.
        next_head = None # Stores the head of the next segment i.e.

        # As long as we have a valid head
        while temp_head:

            # Get the kth node:
            curr = self.getKthNode(temp_head, k)

            # Last node reached before finishing k
            # Leave it as it is
            if not curr:
                break

            # The kth node becomes the end of the segment
            temp_tail = curr
            # The (k+1)th node becomes the head of the next segment
            next_head = curr.next
            
            # If first traversal store the head that will be returned
            if first_reversal:
                head = temp_tail
                # Set the flag to false for the next reversals
                first_reversal = False
            # If it isn't the first reversal
            else:
                # Stitch the segments. Tail of the previous segment
                # should point to the tail of the current segment.
                prev_tail.next = temp_tail

            # Reverse the segment and get the curr node
            curr = self.reverseList(temp_head, temp_tail, next_head)

            # Since the segment is reversed, the head of the previous segment
            # becomes the tail of the previous segment
            prev_tail = temp_head
            # Curr node becomes the head of the current segment
            temp_head = curr

        return head


    def reverseList(self, head, tail, next_head):
        prev, curr = next_head, head
        stop = tail.next

        while curr != stop:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return curr

    def getKthNode(self, temp_head, k):
        count = 1
        curr = temp_head
        while curr and count < k:
            curr = curr.next
            count += 1
        
        return curr