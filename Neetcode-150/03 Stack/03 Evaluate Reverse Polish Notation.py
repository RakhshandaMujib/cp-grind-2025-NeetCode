# Title: Evaluate Reverse Polish Notation
# Link: https://neetcode.io/problems/evaluate-reverse-polish-notation
# Difficulty: Medium 
# Tags: Stack

class Solution:
    def isOperator(self, token) -> bool:
        # Check if the given token is an operator
        return token in {'+', '-', '*', '/'}
    
    def evalExp(self, operator, left_operand, right_operand) -> int:
        # Convert the str operands to int
        left_operand = int(left_operand)
        right_operand = int(right_operand)

        # Evaluate and return the expression depending on the operator
        if operator == '+':
            return left_operand + right_operand
        elif operator == '-':
            return left_operand - right_operand
        elif operator == '*':
            return left_operand * right_operand
        elif operator == '/':
            # Truncate it to 0
            return int(left_operand / right_operand)

    def evalRPN(self, tokens: List[str]) -> int:
        '''
        Approach:
        * Push the integers.
        * On encountering an operator, pop the top 2 integers - 
          right operand gets popped first followed by the
          left operand.
        * Evaluate the expression.
        * Push the expression to the stack.
        '''

        # Edge case: Only one integer in the tokens
        if len(tokens) <= 1:
            return(int(tokens[0]))

        stack = []
        left_operand, right_operand = 0, 0
        exp = 0

        for token in tokens:
            if not self.isOperator(token):
                stack.append(token)
            else:
                right_operand = stack.pop()
                left_operand = stack.pop()
                exp = self.evalExp(token, left_operand, right_operand)
                stack.append(exp)

        return stack.pop()