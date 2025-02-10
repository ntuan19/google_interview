'''
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

from collections import defaultdict
class Solution:
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

        
