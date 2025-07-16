# Title: Products of Array Except Self
# Link: https://neetcode.io/problems/products-of-array-discluding-self
# Difficulty: Medium 
# Tags: Arrays, Hashing

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize prefix and postfix products
        prod_prefix, prod_postfix = 1, 1

        # Arrays to store cumulative prefix and postfix products
        prefix_prod, postfix_prod = [], []

        # Reverse of input array for easier postfix processing
        nums_rev = list(reversed(nums))

        # Placeholder for each index's final product (excluding self)
        result_prod = 1
        result = []

        # Step 1: Compute prefix and postfix products
        for i in range(len(nums)):
            # Build prefix product array (left to right)
            prod_prefix *= nums[i]
            prefix_prod.append(prod_prefix)

            # Build postfix product array (right to left via reversed list)
            prod_postfix *= nums_rev[i]
            postfix_prod.append(prod_postfix)

        # Reverse the postfix product array to align it with the original indices
        postfix_prod.reverse()

        # Step 2: Calculate result by multiplying prefix and postfix products
        for i in range(len(nums)):
            if i == 0:
                # First element: No prefix product, so take postfix from i+1
                result_prod = postfix_prod[i + 1]
            elif i == len(nums) - 1:
                # Last element: No postfix product, so take prefix from i-1
                result_prod = prefix_prod[i - 1]
            else:
                # Middle elements: Multiply prefix and postfix around index i
                result_prod = prefix_prod[i - 1] * postfix_prod[i + 1]

            result.append(result_prod)

        return result
