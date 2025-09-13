# Title: Find Minimum in Rotated Sorted Array
# Link: https://neetcode.io/problems/find-minimum-in-rotated-sorted-array
# Difficulty: Medium 
# Tags: Binary Search


'''
Approach 2:

At each step, ask:
Is middle bigger than right? → Go right.
Else → Go left (keep mid).
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Search space is the whole array
        l, r = 0, len(nums) - 1

        # Use < because we keep mid in the search space (with r = m).
        while l < r:
            m = (l + r) // 2

            # If mid is in the right-rotated (unsorted) half
            if nums[m] > nums[r]:
                # Minimum must be strictly to the right of mid
                l = m + 1
            else:
                # Mid is in the sorted half (could still be the min)
                r = m

        # When l == r, we've narrowed down to the minimum element
        return nums[l]


'''
Approach 1:
Find the pivot where the mid element is always smaller than 
the element lying to the left or right of it.

class Solution:
    def findMin(self, nums: List[int]) -> int:
       if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1

        while l <= r:
            L, R = nums[l], nums[r]
            m = (l + r) // 2
            M = nums[m]

            if m == 0 and nums[m + 1] > M or \
               m == len(nums) - 1 and nums[m - 1] > M or \
               nums[m + 1] > M < nums[m - 1]:
               return M
            
            if L >= R:
                if M > R:
                    l = m + 1
                else:
                    r = m - 1
            else:
                return L
'''