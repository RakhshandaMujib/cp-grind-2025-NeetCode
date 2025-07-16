# Title: Group Anagrams
# Link: https://neetcode.io/problems/anagram-groups
# Difficulty: Medium 
# Tags: Arrays, Hashing

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a default dictionary where each value is a list.
        # This will map character frequency signatures to lists of anagrams.
        result = defaultdict(list) 

        # Loop through each word in the input list
        for word in strs:
            # Create a 26-length array to count character occurrences (a–z)
            # Each word's count array acts as a unique signature for its 
            # anagram group
            alpha_count = [0] * 26

            # Count the frequency of each character in the word
            for char in word:
                alpha_count[ord(char) - ord("a")] += 1
            
            # Convert the list to a tuple so it can be used as a dictionary key
            # Words with the same character count will share the same key
            result[tuple(alpha_count)].append(word)
        
        # Return all grouped anagrams as a list of lists
        return list(result.values())
