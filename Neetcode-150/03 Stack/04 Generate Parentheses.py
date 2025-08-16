# Title: Generate Parentheses
# Link: https://neetcode.io/problems/generate-parentheses
# Difficulty: Medium 
# Tags: Stack

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        Approach 1: Backtracking + Explicit stack
        - Choices: At each step, we can add '(' or ')'.
        - Constraints (Pruning):
            * Add '(' only if open_count < n.
            * Add ')' only if close_count < open_count.
        - Goal: When open_count == close_count == n -> we found a valid sequence.
        - Undo: After exploring a choice, pop it from the stack to restore state.
        '''

        result = []
        stack = []  # Keeps track of the current sequence of parentheses.

        def backtrack(open_count, close_count):
            # Goal reached: we used all n opens and closes.
            if open_count == close_count == n:
                result.append("".join(stack))
                return
            
            # Choice 1: Add ')' if it won’t break balance.
            if close_count < open_count:
                stack.append(')') # Make choice
                backtrack(open_count, close_count + 1)  # Explore deeper
                stack.pop() # Undo choice (backtrack)

            # Choice 2: Add '(' if we still have opens left.
            if open_count < n:
                stack.append('(') # Make choice
                backtrack(open_count + 1, close_count)  # Explore deeper
                stack.pop() # Undo choice (backtrack)

        # Start the exploration with no parentheses placed yet.
        backtrack(0, 0)
        return result

'''
Approach 2:
No need of explicit pushing-popping with an explicit stack.
Use the call stack of functions.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(curr_str, open_count, close_count):
            if len(curr_str) == 2 * n:
                result.append(curr_str)
            
            if open_count < n:
                backtrack(curr_str + '(', open_count + 1, close_count)
            
            if close_count < open_count:
                backtrack(curr_str + ')', open_count, close_count + 1)
            
        backtrack("", 0, 0)

        return result
'''