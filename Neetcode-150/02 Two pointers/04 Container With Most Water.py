# Title: Container With Most Water
# Link: https://neetcode.io/problems/max-water-container
# Difficulty: Medium 
# Tags: Two-pointer

class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # Make the pointers point to the farthest ends:
        left_p, right_p = 0, len(heights) - 1
        
        max_vol = 0

        while left_p < right_p:

            # Get the heights of the bars:
            left_ht, right_ht = heights[left_p], heights[right_p]
            
            # Compute the offsets. 
            # Think hor_offset is the length and 
            # ver_offset is the breadth of a rectangle.
            hor_offset = right_p - left_p
            ver_offset = min(left_ht, right_ht)
            
            # Compute the current volume:
            curr_vol = hor_offset * ver_offset
            
            # Update the max volume:
            max_vol = max(curr_vol, max_vol)
            
            if left_ht < right_ht:
                # Move left_p inward if left_ht is smaller.
                left_p += 1
            else:
                # Move right_p inward otherwise
                right_p -= 1


        return max_vol