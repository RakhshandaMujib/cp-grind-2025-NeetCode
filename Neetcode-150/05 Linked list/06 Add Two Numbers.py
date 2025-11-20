# Title: Add Two Numbers
# Link: https://neetcode.io/problems/add-two-numbers
# Difficulty: Medium 
# Tags: Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        ans = dummy
        carry = 0

        # Eg. 5 + 5 = 10 ([0, 1]) 
        # Loop should execute even if there is a carry
        while l1 or l2 or carry:

            # If there is a mismatch in the number of digits,
            # add a leading 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sum_val = v1 + v2 + carry
            carry = sum_val // 10
            ans.next = ListNode(sum_val % 10)

            # Progress the pointers:
            ans = ans.next
            # If there is a mismatch in the lengths, one of the pointers
            # will be None before the other. If it is None, let it be,
            # progress the other pointer. 
            # Also, if both the pointers are None, let it be but 
            #  we need the loop to execute once more to handle the carry.
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
            

    # Approach 1:
    '''def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        a = dummy # answer points to the dummy
        carry = 0

        while l1 and l2:
            sum_val = l1.val + l2.val + carry
            carry = sum_val // 10
            a.next = ListNode(sum_val % 10)

            if not l1.next and l2.next:
                l1.next = ListNode(0)
            elif l1.next and not l2.next:
                l2.next = ListNode(0)
            
            l1 = l1.next
            l2 = l2.next
            a = a.next
        
        if carry:
            a.next = ListNode(1)
        
        return dummy.next'''