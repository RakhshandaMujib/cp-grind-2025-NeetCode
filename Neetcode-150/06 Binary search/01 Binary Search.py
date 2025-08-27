# Title: Binary Search
# Link: https://neetcode.io/problems/binary-search
# Difficulty: Easy 
# Tags: Binary Search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Approach 1: Recursive approach
        '''
        left_p = 0
        right_p = len(nums) - 1

        def binary_search(left_p, right_p) -> int:
            mid_p = (left_p + right_p) // 2
            mid_num = nums[mid_p]
            
            # Base codition:
            if left_p > right_p:
                return -1

            # Update the pointers if target is not found
            if mid_num > target:
                # Move the right_p leftwards
                return binary_search(left_p, mid_p - 1)
            elif mid_num < target:
                # Move the left_p rightwards
                return binary_search(mid_p + 1, right_p)
            else:
                # Return the index if target is found
                return mid_p
        
        return binary_search(left_p, right_p)


    '''
    Approach 2: Iterative Approach

    def search(self, nums: List[int], target: int) -> int:
        left_p = 0
        right_p = len(nums) - 1

        while left_p <= right_p:

            # Compute the mid_p and get the mid element
            mid_p = (left_p + right_p) // 2
            mid_num = nums[mid_p]

            if mid_num > target:
                # Move the right_p leftwards
                right_p = mid_p -1

            elif mid_num < target:
                # Move the left_p rightwards
                left_p = mid_p + 1

            else: # Target found at mid_p
                return mid_p
        else:
            return -1 # Target is absent in the list'''
        