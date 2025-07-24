# Title: Valid Sudoku
# Link: https://neetcode.io/problems/valid-sudoku
# Difficulty: Medium 
# Tags: Arrays, Hashing

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Initialize empty hash maps for keeping track of 
        #the set of numbers in all 9 rows, columns, and 
        #square grids.

        #{row_ID : {set of numbers in the row}}
        row_set = defaultdict(set) 
        #{col_ID : {set of numbers in the col}}
        col_set = defaultdict(set) 
        #{(sq_row_ID, sq_col_ID) : {set of numbers in the square}}
        sq_set = defaultdict(set) 

        for row in range(9):
            for col in range(9):
                item = board[row][col]

                #The sq index will be as followed:
                sq_row, sq_col = row // 3, col // 3

                #Skip the empty items
                if item == ".":
                    continue

                #Check if them is present in any of the hashmaps:
                if item in row_set[row] or\
                 item in col_set[col] or\
                 item in sq_set[(sq_row, sq_col)]:
                    return False
                
                #Add the items to the hashmaps:
                row_set[row].add(item)
                col_set[col].add(item)
                sq_set[(sq_row, sq_col)].add(item)
        
        #Once the entire grid is scanned succefully, return True
        return True


                


