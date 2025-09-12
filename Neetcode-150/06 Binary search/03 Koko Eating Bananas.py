# Title: Koko Eating Bananas
# Link: https://neetcode.io/problems/eating-bananas
# Difficulty: Medium 
# Tags: Binary Search

import numpy as np

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # If the hours allowed is the same as the number of piles
        # k should be big enough to finish the biggest pile.
        if len(piles) == h:
            return max(piles)
        
        # Lower bound for k should be at least the average
        l = int(np.ceil((sum(piles)/h)))
        # Upper bound for k should be the max #bananas
        r = max(piles)
        answer = r

        # Perform binary search to find the optimal 
        # value of k
        while l <= r:
            k = (l + r) // 2
            # Track the hours consumed with the current k
            hours = 0
            for bananas in piles:
                hours += int(np.ceil(bananas/k))
                if hours > h:
                    # Hours consumed exceeded the h allowed
                    # with the current k, i.e. k is too small.
                    # Update the search space so that k can get 
                    # bigger values.
                    l = k + 1 
                    break

            if hours <= h:
                # Even if the hours consumed is less than h
                # there's a chance it might not be optimal.
                answer = k  # Store the current best value of k  
                # Look for smaller values of k.
                r = k - 1

        return answer