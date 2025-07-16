# Title: Encode Decode Strings
# Link: https://neetcode.io/problems/string-encode-and-decode
# Difficulty: Medium 
# Tags: Arrays, Hashing

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            # Encoding scheme: Metadata + word.
            # Metadata is the the count of chars to consume 
            # followed by any delimiter.
            # Note: Use prefix not suffix to avoid consuming
            # the data. We only need the metadata for decoding.
            result += f'{len(word)}+' + word
        return result

    def decode(self, s: str) -> List[str]:
        result = [] # Holds the final list of words
        word = "" # Holds the current word once formed
        i = 0 
        count = 0 # The number of chars to consume

        while i < len(s):
            # If the char is a number
            if s[i].isdigit():
                # Build the count from the metadata
                count *= 10 
                count += int(s[i])
            # Once we get the delimiter, '+' in this case
            if s[i] == '+':
                # Form the word:
                # The word begins from the next index after 
                # the '+' and goes till the count of letters
                # in that word
                word += s[i + 1 : i + count + 1]
                # Append the word to the result
                result.append(word)
                # Skip all the letters of the word
                i += count
                # Reset the placeholders
                count = 0
                word = ""
            # Move to the next character
            i += 1

        return result