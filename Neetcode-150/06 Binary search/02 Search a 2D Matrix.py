# Title: Search a 2D Matrix
# Link: https://neetcode.io/problems/search-2d-matrix
# Difficulty: Medium 
# Tags: Binary Search

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_rows, n_cols = len(matrix), len(matrix[0])
        
        # Step 1: Binary search on rows (first and last column only)
        start, end = 0, n_rows - 1
        row = -1
        while start <= end:
            mid = (start + end) // 2

            # If the target falls in the current row, break
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            # If the target is greater than the first element
            # of the mid row, push the end row up.
            elif matrix[mid][0] > target:
                end = mid - 1
            # If the target is smaller than the first element 
            # of the mid row, or it is larger than the last 
            # element of the mid row, push the start down.
            else:
                start = mid + 1
        
        # Target not in any row range
        if row == -1:
            return False
        
        # Step 2: Binary search inside the found row
        start, end = 0, n_cols - 1
        while start <= end:
            mid = (start + end) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        # Matrix is scanned, element is not found 
        return False