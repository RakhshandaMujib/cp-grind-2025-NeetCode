# Title: Copy Linked List with Random Pointer
# Link: https://neetcode.io/problems/copy-linked-list-with-random-pointer
# Difficulty: Medium 
# Tags: Linked List

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return 

        # Step 1: Interleave such that-- 1->1'->2->2'...
        curr = head

        while curr:
            # Create the copy node
            copy = Node(curr.val)
            # Store the old next of the curr node
            old_next = curr.next
            # Insert copy between the curr and old_next
            curr.next = copy
            copy.next = old_next
            # Iterate to the old_next
            curr = old_next
        
        # Step 2: Assign the random pointers to the copy nodes
        curr = head

        while curr:
            if curr.random:
                # If the curr node's random is NOT pointing to NULL
                curr.next.random = curr.random.next
            # Iterate to the next old_node
            curr = curr.next.next
        
        # Step 3: Unzip the new list from the old one
        curr = head
        dummy = Node(0)
        copy_curr = dummy

        while curr:
            # Get the copy node
            copy = curr.next
            # Get the old next node
            old_next = copy.next
            # Break: curr->copy. Update the curr_next as the old next
            curr.next = old_next
            # Append the copy node to the copy_curr
            copy_curr.next = copy
            # Progress the current nodes
            copy_curr = copy_curr.next
            curr = curr.next

        return dummy.next