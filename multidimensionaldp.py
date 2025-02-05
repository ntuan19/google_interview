
from typing import List
class Solution:
    def triangle(self,triangle:List[List[int]]) -> int:
        '''
        So the problem triangle, 
        we can do this problem by starting with index 
        i= 0
           -> two choices : stay or move to the next one. 
        '''
        n = len(triangle)
        queue = deque([(0,triangle[0][0],0)])
        min_path = float("inf")
        while queue:
            current_indx,total,row = queue.popleft() 
            if row == n-1:
                min_path= min(min_path,total) 
                continue
            if row< n-1:
                for i in range(0,2):
                    if current_indx +i < len(triangle[row+1]):
                       queue.append((current_indx+i,total+triangle[row+1][current_indx+i],row+1))
        return min_path
    
    def triangle_minimum(self,triangle:List[List[int]]) -> int:
        '''
        This solution is similar to the previous solution. However, instead of using bfs,
        it uses bottom up approach.
               2
              2 1
             2 3 4 -> starting row
            5 1 3 4
        We start from the bottom +1 row. 
        With this starting row, we go through all elements of this row and update it in-place
        by seeing which values it can take from the row below it.
        Calculation : 2 + min(5,1) = 3
                      3 + min(1,3) =4 
                      4 + min(3,4) = 7
        Continue doing so will get us to the top result.
        '''
        n = len(triangle)
        
        for row in range(n-2,-1,-1):
            for col in range(len(triangle[row])):
                triangle[row][col] = triangle[row][col] + min(triangle[row+1][col],triangle[row+1][col+1])
        return triangle[0][0]    
    
    def minimum_path_sum(self,grid:List[List[int]]) -> int:
        '''
        question 64 on leetcode.
        regarding this problem, we can update the grid in-place.
        1. if the cell is on the first row -> then its sum is current_cell + left-side cell sum 
        2. if the cell is on the first col -> then its sum is current_cell + its top cel sum 
        3. else, it would be the the min betweeen its cell above (directly) and its its left-side cell  
        '''
        row = len(grid) 
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    continue 
                elif i == 0:
                    grid[i][j] += grid[i][j-1] 
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] = grid[i][j] + min(grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]              
    
    def uniquePathsWithObstacles(self,obstacleGrid:List[List[int]]):
        #we have a function to check the palindrome 
        pass
    
    def longestPalindrome(self,s):
        longest_string = ""
        def expandAroundCenter(left:int,right:int)-> str:
            while left >=0 and right < len(s) and s[left] == s[right]:
                left-=1
                right+=1
            return s[left:right]
        
        for i in range((len(s))):
            p1 = expandAroundCenter(i,i)
            p2 = expandAroundCenter(i,i+1)
            longest_string= max(p1,p2,longest_string,key=len)
        return longest_string
    
    def isInterLeave(s1:str,s2:str,s3:str) -> bool:
        if len(s1) + len(s2) != len(s3): return False 
        dp = {}

        def dfs(i,j,k):
            #base case: if we reach the end of both s1 and s2, we succeed
            if i == len(s1) and j == len(s2):
                return True 
            if i == len(s1):
                return s2[j:] == s3[k:]
            if j == len(s2):
                return s1[i:] == s3[k:]
            if (i,j) in dp:
                return dp[(i,j)]
            
            res = (
               ( 
                s1[i] == s3[k] and dfs(i+1,j,k+1)) or (s2[j]==s3[k] and dfs(i,j+1,k+1)
               )
            )
            return res 
        return dfs(0,0,0)




