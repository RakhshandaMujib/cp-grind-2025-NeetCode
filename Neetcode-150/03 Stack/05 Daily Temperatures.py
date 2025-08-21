# Title: Daily Temperatures
# Link: https://neetcode.io/problems/daily-temperatures
# Difficulty: Medium 
# Tags: Stack

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, curr_temp in enumerate(temperatures):
            # While the stack is non-empty, and the 
            # the curr_temp > previous temps
            # pop the indices of the previous temps
            # and update the result for that index.
            while stack and curr_temp > temperatures[stack[-1]]:
                prev_i = stack.pop()
                # Difference between the current index (which is 
                # where the 'just' greater temp is at) and the prev_i 
                # gives the offset of finding the next hotter day.
                result[prev_i] = i - prev_i
            # Push when the curr_temp < temperatures in the stack.
            stack.append(i)

        return result