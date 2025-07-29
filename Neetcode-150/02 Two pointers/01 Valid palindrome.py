# Title: Valid Palindrome
# Link: https://neetcode.io/problems/is-palindrome
# Difficulty: Easy 
# Tags: Two-pointers

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # The string might contain special characters so we need to clean it
        clean_string = str()

        for char in s:
            if ord('a') <= ord(char) <= ord('z') or\
               ord('0') <= ord(char) <= ord('9'):
               clean_string += char

            elif ord('A') <= ord(char) <= ord('Z'):
               clean_string += char.lower()

        # Two-pointers approach helps in saving space. 
        # Initialize the two pointers at the start and end of the string.
        start_p = 0
        end_p = len(clean_string) - 1
        
        # Iterate through the entire string:
        while start_p <= end_p:
            # In case of mismatch, return false
            if clean_string[start_p] != clean_string[end_p]:
                return False

            # start_p moves forward, end_p moves backward.
            start_p += 1
            end_p -= 1
        
        # Positive case
        return True