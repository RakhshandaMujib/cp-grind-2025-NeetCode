# Title: Two sum
# Link: https://neetcode.io/problems/two-integer-sum-ii
# Difficulty: Medium 
# Tags: Two-pointer

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #Initialize the pointers
        low_p = 0 #Goes from L-R
        high_p = len(numbers) - 1 #Goes from R-L

        #Iterate through the list from both the ends:
        while low_p < high_p:
            
            #Compute the current sum
            curr_sum = numbers[low_p] + numbers[high_p]
            
            # Match found:
            if curr_sum == target:
                return [low_p + 1, high_p + 1]
            
            elif curr_sum < target:
                # Move the low_p to the next cell
                low_p += 1

            else:
                # Current sum is more than the target
                # Move the high_p to the previous cell
                high_p -= 1