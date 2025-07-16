# Title: Two sum
# Link: https://neetcode.io/problems/two-integer-sum
# Difficulty: Easy 
# Tags: Arrays, Hashing

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ind = {} #Holds the indices of the difference observed

        for i in range(len(nums)):
            num = nums[i]
            diff = target - num

            #Check if the diff is already present in the hashmap
            if diff in ind.keys():
            	#Return the index of the difference and the current
            	#index, the numbers at which would sum up to the target
                return [ind[diff], i]
            else:
            	#Add the current number in the hashmap with the index
            	#if the difference is not found so that in the future
            	#if a complement comes, we can pick this up.
                ind[num] = i
                
        return None