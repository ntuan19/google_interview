'''
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. 
You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around 
the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.


 gas  [1,  2, 3, 4, 5]
 cost [3,  4, 5, 1, 2]
      [-2,-2,-2, 3, 3]
So, we subtract the difference between gas on at station ith vs the cost to drive to that ith station.
Here, we found that at station 4th, the cost is smaller than gas, meaning we can start from this index
However, when i introduce more station and gas, we can see that index 4 no longer works
because we need to ensure that from index 4 to the the rest of stations, it needs to have
positive gases compared to cost. 


 gas  [1,  2, 3, 4, 5, 1,1,11]
 cost [3,  4, 5, 1, 2, 6,4,1]
      [-2,-2,-2, 3, 3,-6,-4,10]

The idea is as such, we try to see the difference between gas and cost.
Whenever the diff is positive, we record the station ith as the starting position(I)
We continue to traverse and adding diff to our total(with total summing total diff from 
recored starting point (I))
If at any point, the total is negative, we make the starting point empty and reset the total to 0.


'''
from typing import List 
class Solution:
    def canCompleteCircuit(self,gas: List[int], cost: List[int]) -> int:
        diff = 0 
        total = 0 
        start = None 
        total_tank = 0
        for i in range(len(gas)):
            diff = gas[i]-cost[i] 
            total += diff  
            total_tank += diff
            if start == None:
                if total_tank >= 0:
                    start = i   
                else:
                    total_tank = 0
            elif start !=None and total_tank <0 :
                start = None
                total_tank = 0
        return start if total >=0 else -1

    def test_canCompleteCircuit(self):
        assert self.canCompleteCircuit([5,1,2,3,4],[4,4,1,5,1]) == 4, "Test failed" 
        assert self.canCompleteCircuit([1,  2, 3, 4, 5, 1,1,11],[3,  4, 5, 1, 2, 6,4,1]) == 7, "Test failed, should be 7"
        assert self.canCompleteCircuit([2,3,4],[3,4,3]) == -1, "Test failed, should be -1"
solution = Solution()
solution.test_canCompleteCircuit()


