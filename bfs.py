'''
https://leetcode.com/problems/shortest-distance-from-all-buildings/?envType=company&envId=apple&favoriteSlug=apple-six-months

You are given an m x n grid grid of values 0, 1, or 2, where:

each 0 marks an empty land that you can pass by freely,
each 1 marks a building that you cannot pass through, and
each 2 marks an obstacle that you cannot pass through.
You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
So return 7.
Example 2:

Input: grid = [[1,0]]
Output: 1
Example 3:

Input: grid = [[1]]
Output: -1



'''
from collections import deque, defaultdict 
class BFSSolution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        '''
        Start with the cloned grid 
        numberOfbuildings = 0 
        Start the dfs on each of the cell that has value of 1. 
        If the cell is 0 -> continue to go explore and update the value of (numberOfbuildings, distance) into the cloned grid. 

         1 0 2 
         0 0 0 
         0 0 1 
           |(1,4)|
      (1,4)|(1,4)|(2,4)|
      (1,3)|(2,4)|.    |
        '''
        row = len(grid)
        col = len(grid[0])
        cloned_grid = [[(0,0) for i in range(col)] for j in range(row)]
        numberOfbuildings = 0
        def explore(i,j):
            nonlocal cloned_grid
            queue = deque([(i,j,0)])
            visited = set()
            visited.add((i,j))
            while queue:
                rowInd,columnInd,distance = queue.popleft()
                for newRowInd, newColInd in [[rowInd+1,columnInd],[rowInd-1,columnInd],[rowInd,columnInd-1],[rowInd,columnInd+1]]:
                    if 0 <= newRowInd < row and 0 <= newColInd< col:
                        if grid[newRowInd][newColInd] == 0 and (newRowInd,newColInd) not in visited:
                            queue.append([newRowInd,newColInd,distance+1])
                            visited.add((newRowInd,newColInd))
                            count, currDistance = cloned_grid[newRowInd][newColInd] 
                            cloned_grid[newRowInd][newColInd] = numberOfbuildings if count +1 == numberOfbuildings else count, currDistance + distance +1 
                        else:
                            visited.add((newRowInd,newColInd))
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    numberOfbuildings +=1 
                    explore(i, j)
        min_val = float("inf")
        for i in range(row):
            for j in range(col):
                if cloned_grid[i][j][0] == numberOfbuildings and numberOfbuildings != 0:
                    min_val = min(min_val,cloned_grid[i][j][1])
        return min_val if min_val != float("inf") else -1 

    def networkDelayTime(self,times,n,k) -> int:
        '''
        This problem asks if a signal from a node A can traverse and reach all other nodes in the network and if it does,
        what is the least minimum time it needs to reach the all the nodes. 
        So, what we use is a dijkstra algorithm to keep track of the min distance.
        Use a minheap and append the (distance,node) into the heap
        Another array/dictionary keeping track of the min distance needed to reach that node.
        We pop the distance, node from the minheap. Checking node's neighbours and compare to see if 
        the current distance in array is larger than the new distance, then we update the new distance
        and append it into the heap.
        '''
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        
        #step 2: Initialize minheap and distance dictionary
        min_heap = [(0,k)] #time,node
        dist = {i:float("inf") for i in range(1,n+1)}
        dist[k] = 0 
        while min_heap:
            time,node = heapq.heappop(min_heap)
            for neigbhour,extra in graph[node]:
                if time + extra < dist[neighbour]:
                    dist[neigbhour] = time + extra
                    heapq.heappush(min_heap,(time+extra,neighbour))
        ans =  max(dist.values())
        return ans if ans != float("inf") else -1  
    
