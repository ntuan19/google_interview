'''
https://leetcode.com/problems/sort-matrix-by-diagonals/description/
Sort Matrix by Diagonals
You are given an n x n square matrix of integers grid. Return the matrix such that:

The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order.
The diagonals in the top-right triangle are sorted in non-decreasing order.

So if we use two loops, and going through the 2DArray, the to identify cells belonging 
to a certain diagnal, we use the difference between i-j/ or j-i.

      0 | 1| 2|
    0|0 |-1|-2|
    1|1 |0 |-1|
    2|2 |1 | 0|

    -> Another solution 
'''

from typing import List 
from collections import defaultdict
class MatrixSolution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        '''
        Two dictionaries, one containing bottom-left triangle and the other containing top-right triangle. 
        Go through all the cells on the first column ->
          - create a dictionary with key as original cell and value as adjacent diagonally cells. 
          - simiarly, create a dictionary with key (except (0,0)) 
        Record the values and sort those values
        ''' 
        bottom_left = defaultdict(list)
        bottom_left_values = defaultdict(list)
        top_right = defaultdict(list)
        top_right_values = defaultdict(list)

        for i in range(0,len(grid)):
            #Append cells onto the bottom_left 
            currX,currY = i,0 
            # bottom_left[(currX,currY)].append([currX,currY])
            k = 0
            while 0<= currX+k< len(grid) and 0<= currY+k< len(grid[0]):
                   bottom_left[(currX,currY)].append([currX+k,currY+k])
                   bottom_left_values[(currX,currY)].append(grid[currX+k][currY+k])
                   k+=1
            #Append cells onto the top right 
            currX, currY = 0,i 
            k = 0
            if currY != 0:
                while 0<= currX+k< len(grid) and 0<= currY+k< len(grid):
                    top_right[(currX,currY)].append([currX+k,currY+k])
                    top_right_values[(currX,currY)].append(grid[currX+k][currY+k])
                    k+=1

        # Sort and update bottom-left diagonals
        for key, val in bottom_left.items():
            sorted_values = sorted(bottom_left_values[key])[::-1]  # Sort the values
            for i in range(len(val)):
                x,y = val[i][0],val[i][1]
                grid[x][y] = sorted_values[i]

        for key, val in top_right.items():
            sorted_values = sorted(top_right_values[key]) # Sort the value
            for i in range(len(val)):
                x,y = val[i][0],val[i][1]
                grid[x][y] = sorted_values[i]
        return grid
    
    def sortMatrixSmarter(self,grid:List[List[int]]) -> List[List[int]]:
        dic_values = defaultdict(list)
        dic_positions = defaultdict(list)

        for i in range(len(grid)):
            for j in range(len(grid)):
                d = i -j 
                dic_values[d].append(grid[i][j])
                dic_positions[d].append([i,j])
       
        for key,val in dic_values.items():
            if key < 0:
                val.sort()
            else:
                val.sort(reverse =True)
        
        for key,val in dic_positions.items():
            for i in range(len(val)):
                grid[val[i][0]][val[i][1]] = dic_values[key][i]
        return grid
    
    def isValidSudoku(self,board:List[List[int]]) -> bool:
        '''
        The point of soduku is being able to check if within the same row,col or within a box, 
        it contains distinct values
        '''
        rows = len(board)
        cols = len(board)
        dic_rows = defaultdict(set)
        dic_cols = defaultdict(set)
        dic_boxes = defaultdict(set)

        for i in range(rows):
            for j in range(cols):
                cell = board[i][j]
                if cell == ".":
                    continue
                if cell in dic_rows[i]:
                    return False 
                if cell in dic_cols[j]:
                    return False 
                if cell in dic_boxes[(i//3,j//3)]:
                    return False 
                dic_rows[i].add(cell)
                dic_cols[j].add(cell) 
                dic_boxes[(i//3,j//3)].add(cell)
        return True 


test = MatrixSolution()
print(test.sortMatrixSmarter([[1,7,3],[9,8,2],[4,5,6]]) ==  [[8,2,3],[9,6,7],[4,5,1]])
print(test.isValidSudoku([[1,7,3],[9,8,2],[4,5,6]]) ==  True)
print(test.isValidSudoku(board=[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]) == True)
print(test.isValidSudoku(board=[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]) == False)


        
'''
tic tac toe game.

In the grid of n x n, 
To find all the values of the main diagonal 
-> we can see if row == col 
To find all values of the anti-main diagonal :
-> find row + col == N-1 

To capture all diagonals (not just the main and anti-diagonal but all possible diagonals), you can use two different dictionary mappings:

For top-left to bottom-right diagonals (\)
Key: row - col
Cells with the same row - col belong to the same diagonal.
For top-right to bottom-left diagonals (/)
Key: row + col
Cells with the same row + col belong to the same anti-diagonal.
'''
def tictactoe(moves: List[List[int]]) -> str:
        '''
        check for row, col or diagonal line to see if there is any three lines having the same symbols -> yes, return the symbol. 
        check if there is any pending spot -> yes -> 
        '''
        free_spots = False  
        dic_rows = defaultdict(list)
        dic_cols = defaultdict(list)  
        main_diagonal = []
        anti_diagonal = []
        turn = False  #meaning A
        if len(moves) < 9:
            free_spots = True 
        for move in moves:
            row, col = move[0],move[1]
            if turn == False:
                symbol = "A"
            else:
                symbol = "B"
            dic_rows[row].append(symbol)
            dic_cols[col].append(symbol)
            if row +col ==2:
                anti_diagonal.append(symbol)
            if row == col:
                main_diagonal.append(symbol)
            if len(dic_cols[col]) == 3 and len(set(dic_cols[col])) ==1:
                return symbol
            if len(dic_rows[row]) == 3 and len(set(dic_rows[row])) ==1:
                return symbol
            if len(anti_diagonal) ==3 and len(set(anti_diagonal)) ==1:
                return symbol
            if len(main_diagonal) ==3 and len(set(main_diagonal)) ==1:
                return symbol
            turn = not turn
        if len(moves) == 9:
            return "Draw"
        if free_spots == True:
            return "Pending"


