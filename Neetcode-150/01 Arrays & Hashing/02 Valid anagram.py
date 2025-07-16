# Title: Valid Anagram
# Link: https://neetcode.io/problems/is-anagram
# Difficulty: Easy 
# Tags: Arrays, Hashing

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    	# Create a hash map for both the strings with 
    	# the counts being the value and the letter being
    	# the key
        s_dict = {i : s.count(i) for i in s}
        t_dict = {i : t.count(i) for i in t}
        
        return s_dict == t_dict