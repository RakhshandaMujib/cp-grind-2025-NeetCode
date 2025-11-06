# Title: Median of Two Sorted Arrays
# Link: https://neetcode.io/problems/median-of-two-sorted-arrays
# Difficulty: Hard 
# Tags: Binary Search


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        
        # Let A be the smaller array
        if len(A) > len(B):
            A, B = B, A
        
        total_len = len(A) + len(B)
        # Adding 1 to half to handle odd and even cases better
        # If the length of the combined arrays is odd, the median
        # would be the right-most element of the left half i.e.
        # max(left). 
        half_len = (total_len + 1) // 2

        # Perform BS on A to look for the correct partition

        # Since the partitions can lie at len(A) + 1 positions
        # Eg: | 1 | 2| --> For a length of 2, 3 places are possible
        # so, right_p will not be len(A) - 1 but len(A)
        left_p, right_p = 0, len(A) 

        while left_p <= right_p:
            partition_A = (left_p + right_p)// 2
            # The left half of the combined arrays will have
            # half number of elements.So, partition_B will have
            # half_len - partition_A number of elements.
            partition_B = half_len - partition_A

            # If the partitions happen to be at the ends, have
            # placeholders for comparisons of left-right elements.
            A_left = A[partition_A - 1] if partition_A > 0 else float('-inf')
            A_right = A[partition_A] if partition_A < len(A) else float('inf')
            B_left = B[partition_B - 1] if partition_B > 0 else float('-inf')
            B_right = B[partition_B] if partition_B < len(B) else float('inf')

            # Found the correct partitions for both the arrays:
            if A_left <= B_right and B_left <= A_right:
                if total_len % 2: # Odd
                    # Since the right-most element of the 
                    # left half of the combined array
                    # will have the median.
                    return max(A_left, B_left)
                else: # Even
                    # Median would be the mean of the right-most (max) element
                    # of the left half and the left-most element (min) of the
                    # right half.
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
            
            # Partition is right-ward from ideal partition.
            elif A_left > B_right:
                # Move right_p left-ward:
                right_p = partition_A - 1
            
            # Partition is left-ward from ideal partition.
            else: # B_left > A_right:
                # Move left_p right-ward:
                left_p = partition_A + 1