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

            # If the current number > 0, there is no way
            # we can form a 0 by adding anything up to it
            # (but we can have >= 3 0s in which case [0 0 0]
            # will be a valid triplet, so not using >= 0)
            if curr_num > 0:
                return result

            target_sum = 0 - curr_num
            
            # We are not looking at the first number
            # and, the previous number is not the same
            # as the current number to avoid duplicate triplets
            if i > 0 and nums[i - 1] == curr_num: 
                continue
            
            left_p, right_p = i + 1, len(nums) - 1
            
            while left_p < right_p:
                curr_sum = nums[left_p] + nums[right_p]

                # Move inwards
                if curr_sum < target_sum:
                    left_p += 1
                elif curr_sum > target_sum:
                    right_p -= 1

                # Current sum == target sum
                else:
                    # Successful triplet found
                    result.append([curr_num, nums[left_p], nums[right_p]])
                    
                    # Move to look for other 2-sum pair that will make a
                    # valid triplet for the current number
                    left_p += 1

                    # Handle duplicate pairs in the 2-sum:
                     # Skip the duplicate left numbers (or right numbers, any one)
                     # No need of handling the right number duplicates because
                     # a + b will never be equal to c + b if a != c
=                    while nums[left_p] == nums[left_p - 1] and left_p < right_p:
                        left_p += 1

        return result