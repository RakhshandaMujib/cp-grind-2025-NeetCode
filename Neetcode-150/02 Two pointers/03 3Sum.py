# Title: 3Sum
# Link: https://neetcode.io/problems/three-integer-sum
# Difficulty: Medium 
# Tags: Two-pointer

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            curr_num = nums[i]

            if curr_num > 0:  # Can't make zero-sum beyond this
                break
            if i > 0 and curr_num == nums[i - 1]:
                continue  # Skip duplicate first numbers

            low_p, high_p = i + 1, len(nums) - 1

            while low_p < high_p:

                three_sum = curr_num + nums[low_p] + nums[high_p]

                if three_sum < 0:
                    low_p += 1

                elif three_sum > 0:
                    high_p -= 1

                else:
                    result.append([curr_num, nums[low_p], nums[high_p]])
                    
                    # Skip duplicates for both pointers
                    while low_p < high_p and nums[low_p] == nums[low_p + 1]:
                        low_p += 1
                    while low_p < high_p and nums[high_p] == nums[high_p - 1]:
                        high_p -= 1
                    
                    # Move inward
                    low_p += 1
                    high_p -= 1
                    
        return result
