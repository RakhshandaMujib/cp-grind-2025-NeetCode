# Title: Minimum Stack
# Link: https://neetcode.io/problems/minimum-stack
# Difficulty: Medium 
# Tags: Stack


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, val: int) -> None:

        # Handle the first element case:
        if not self.stack or not self.min_stack:
            self.stack.append(val)
            self.min_stack.append(val)
            return

        # Update minimum stack if the val is less than the min:
        tos_min_stack = self.min_stack[-1]
        if tos_min_stack >= val:
            self.min_stack.append(val)

        # Push the element in the stack:
        self.stack.append(val)
        
    def pop(self) -> None:

        # If the TOS and TOS-min_stack are the same,
        # pop the TOS-min_stack.
        tos_min_stack = self.min_stack[-1]
        tos = self.top()
        if tos_min_stack == tos:
            self.min_stack.pop()
        
        # Pop from the stack:
        self.stack.pop()

        
    def top(self) -> int:

        # Return the TOS:
        return self.stack[-1]
        
    def getMin(self) -> int:

        # Return the TOS-min_stack:
        return self.min_stack[-1]