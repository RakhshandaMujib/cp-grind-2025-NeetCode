# Title: Largest Rectangle In Histogram
# Link: https://neetcode.io/problems/largest-rectangle-in-histogram
# Difficulty: Hard 
# Tags: Stack

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # Stores the tuple: (height, index)
        max_area = 0 # Can never be negative so 0 is safe
        right_most_end = len(heights) # Used when cleaning the stack

        for i, height in enumerate(heights):
            start = i # Left boundary for the current bar
            #print(f"i --- {i}, height --- {height}")
            
            # Monotonically increasing stack to process
            # the taller bars first:
            while stack and height < stack[-1][0]:
                
                # The TOS cannot extend rightwards if the current
                # height is smaller than it, so we pop it:
                popped_height, popped_i = stack.pop()

                # Compute the width if we must include the current bar
                width = i - popped_i

                # Compute the area of the popped bar
                curr_area = popped_height * width
                #print(f"width = {i} - {popped_i}, height = {height} area = {curr_area}")

                # Update the max_area:
                max_area = max(curr_area, max_area)

                # Update the left boundary to the extended left 
                # boundary:
                start = popped_i

            # When the stack is empty or when we can extend rightwards
            # i.e. the curr height is >= than the TOS. 
            stack.append((height, start))
            print(stack)

        # Clean the stack and compute the areas for the 
        # bars that can extend till the right most end:
        #print("\n\nCleaning up the stack-----")
        while stack:
            popped_height, popped_i = stack.pop()
            curr_area = popped_height * (right_most_end - popped_i)
            #print(f"width = {right_most_end} - {popped_i}, height = {popped_height} area = {curr_area}")
            max_area = max(curr_area, max_area)

        return max_area