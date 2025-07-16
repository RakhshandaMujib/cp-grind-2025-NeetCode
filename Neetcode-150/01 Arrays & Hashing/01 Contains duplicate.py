# Title: Contains Dupllicate
# Link: https://neetcode.io/problems/duplicate-integer
# Difficulty: Easy 
# Tags: Arrays, Hashing

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()

        # Iterate over the list once
        for num in nums:
        	# Check if the current number is already present in the set
        	# i.e., the number is being encountered for a second time
            if num in s:
                return True
            else:
            	#If the current number is not in the set, add it
                s.add(num)
        return False
