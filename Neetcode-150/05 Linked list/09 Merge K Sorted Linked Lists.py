# Title: Merge K Sorted Linked Lists
# Link: https://neetcode.io/problems/merge-k-sorted-linked-lists
# Difficulty: Hard 
# Tags: Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # If no lists are present -_-
        if not len(lists):
            return None
        
        # While we have at least one list
        while len(lists) > 1:
            # Placeholder for temporarily merged lists
            mergedList = []

            # Pick two lists at a time:
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # If i is the index of the last list, let the 2nd list be None
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                # Merge the two lists individually
                mergedList.append(self.mergeTwoLists(l1, l2))
            
            # Update lists with the merged lists
            lists = mergedList
        
        # lists will only have the finally merged & sorted lists
        return lists[0]


    def mergeTwoLists(self, l1, l2):

        # Same old drama. 
        # Use tail to traverse both the lists.
        dummy = ListNode()
        tail = dummy

        # My overconfidence with the 'same old drama'
        # made me boof up with the `and` condition-
        # oversmartly wrote `or` and got humbled.

        # Traverse through both the lists and update the 
        # smaller value.
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        # Whichever is not NULL, let the tail point to that
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        
        return dummy.next