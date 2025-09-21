# Title: Search in Rotated Sorted Array
# Link: https://neetcode.io/problems/find-target-in-rotated-sorted-array
# Difficulty: Medium 
# Tags: Binary Search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_p, right_p = 0, len(nums) - 1
        
        while left_p <= right_p:
            mid_p = (left_p + right_p) // 2
            L, M, R = nums[left_p], nums[mid_p], nums[right_p]

            if M == target:
                # Target found at mid_p
                return mid_p

            if L <= M:
                # L-M is sorted
                if L <= target < M:
                    # Target lies in the sorted array between
                    # left_p and mid_p. 
                    right_p = mid_p - 1
                else:
                    # Target lies in the unsorted array between
                    # mid_p and right_p.
                    left_p = mid_p + 1
            else:
                # L-M is unsorted
                if M < target <= R:
                    # M-R is sorted and target lies between 
                    # mid_p and right_p
                    left_p = mid_p + 1
                else:
                    # Target lies in the unsorted array between
                    # left_p and mid_p.
                    right_p = mid_p - 1
        
        return -1