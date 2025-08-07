# Title: Valid Parentheses
# Link: https://neetcode.io/problems/valid-parentheses
# Difficulty: Easy 
# Tags: Stack

class Solution:
    def isValid(self, s: str) -> bool:

        # #If there is only one bracket, don't even bother processing.
        if len(s) <= 1:
            return False

        # Use a stack for checking the balance
        stack = []
    
        for bracket in s:

            # If it is an opening bracket, add it to the stack
            if bracket in {'[', '(', '{'}:
                stack.append(bracket)
                continue
        
            # If is is a closing bracket and the stack hasn't been initialized
            # i.e., there is no opening bracket for it, return False.
            if not stack:
                return False
            
            # If it is a closing bracket, check the top of the stack (TOS)
            tos = stack[-1]

            # If a matching pair is found, pop the TOS.
            if bracket == ')' and tos == '(' or \
               bracket == ']' and tos == '[' or \
               bracket == '}' and tos == '{':
                stack.pop()
            else: # Not a matching pair
                return False

        # When all the brackets are processed the stack should be empty.
        # Think of "(("
        return not stack

'''
Approach 1: Use hash-map to store the pairs. Takes extra time and space

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        stack = []
        close_open_brackets = {')':'(', ']':'[', '}':'{'}

        for bracket in s:
            opening_brackets = close_open_brackets.values()
            if bracket in opening_brackets:
                stack.append(bracket)
            elif stack and close_open_brackets[bracket] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return not stack


'''
        