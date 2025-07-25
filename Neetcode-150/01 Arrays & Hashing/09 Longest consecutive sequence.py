# Title: Longest Consecutive Sequence
# Link: https://neetcode.io/problems/longest-consecutive-sequence
# Difficulty: Medium 
# Tags: Arrays, Hashing

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Step 1: Convert to a set for O(1) existence checks
        # - Removes duplicates
        # - Lets us check "is x in nums?" in constant time
        nums_set = set(nums)
        
        max_length = 0  # Will store the longest sequence found

        # Step 2: Iterate through all numbers
        for num in nums_set:
            # Step 3: Only start counting if this number is the **start** of a 
            # sequence
            # If num-1 is in the set, then this isn't the first number of a 
            # sequence -> skip it

            # Guarantees we start from sequence beginnings only
            if num - 1 not in nums_set:  
                curr_num = num
                length = 1  # Current sequence length

                # Step 4: Count forward as long as the next number exists
                while curr_num + 1 in nums_set:
                    length += 1
                    curr_num += 1

                # Step 5: Update the max length if this sequence is 
                # the longest so far
                max_length = max(length, max_length)

        # Step 6: Return the longest sequence length found
        return max_length