# Title: Trapping Rain Water
# Link: https://neetcode.io/problems/trapping-rain-water
# Difficulty: Hard 
# Tags: Two-pointer

class Solution:
    def trap(self, height: List[int]) -> int:
        # If no boundary is available water
        # trapped will be 0.
        if len(height) <= 1:
            return 0

        left_p, right_p = 0, len(height) - 1
        left_max, right_max = height[left_p], height[right_p]
        vol_trapped = 0

        while left_p < right_p:
            # Move left_p inward in search of a taller building
            if left_max < right_max:
                left_p += 1
                curr_left_ht = height[left_p]
                # Check for an update in the left_max:
                left_max = max(left_max, curr_left_ht)
                # Compute the water trapped in the position where
                # left_p is at:
                vol_trapped += left_max - curr_left_ht

            # Move right_p inward in search of a taller building
            else:
                right_p -= 1
                curr_right_ht = height[right_p]
                # Check for an update in the right_max:
                right_max = max(right_max, curr_right_ht)
                # Compute the water trapped in the position where
                # right_p is at:
                vol_trapped += right_max - curr_right_ht

        return vol_trapped

    '''
    FAILED Approach 1:
        # Look in one direction only
        # If I am standing on a building then 
        # I look for the next building which has a 
        # height more than me or equal to me.
        # In the mean time, I'll also track the height
        # of the buildings I am passing on my way
        # and trap water in between the current and next tallest
        # building.
        #
        # Fails for the case: [1, 3, 2, 1, 0, 1, 2]
        # When the current pointer is at 3, it will look for something
        # greater than 3 but it will never find it and miss trapping
        # water between the two 2s.

    def trap(self, height: List[int]) -> int:

        if len(height) <= 1:
            return 0

        curr_p, next_p = 0, 1
        smaller_ht_sum = 0
        blocks_crossed = 0
        vol_trapped = 0

        while curr_p < len(height) - 1:
            curr_ht = height[curr_p] 
            next_ht = height[next_p]
            while curr_ht > next_ht and next_p < len(height):#10
                smaller_ht_sum += next_ht 
                blocks_crossed += 1 
                next_p += 1 
                if next_p == len(height):
                    break
                next_ht = height[next_p] 
            ht = min(curr_ht, next_ht) 
            if (ht * blocks_crossed) - smaller_ht_sum > 0: 
                vol_trapped += (ht * blocks_crossed) - smaller_ht_sum 
            curr_p = next_p 
            next_p += 1 
            smaller_ht_sum = 0 
            blocks_crossed = 0 
        
        return vol_trapped
    '''
                


        