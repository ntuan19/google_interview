import heapq
from typing import List
import unittest
class MedianFinder():
    '''
    Given an array of integers, ( not sorted), find the median value.
    Median value is the mid value of array (odd) or the combination of two middle values/2.
    [3,1,4,5,2]

    1/ First approach is to sort this array and check the mid value or two mid values/2 (depending on the type of array- odd/even array)
    2/ Second approach is to use two heap - min heap and max heap. 
        The point is to create two halves - one half contains smaller values 
                                         - the other half contains larger values 
        Due to the property of a heap, then we always have the smallest/largest element at the top of the heap.
        Here is an example:
        [3,1,4,5,2]
        smaller_half 
        bigger_half 
        We start by appending 3 into smaller half -> [3]
                                -> append smallerhalf.pop() -> smaller half = [],bigger half =[3]
                                -> smaller half is smaller than bigger half -> smaller half.append( biggerhalf.pop)
                                -> smaller half = [-3], bigger half = []
                    appending 1 into smaller half:  smaller half: [-3,-1]
                                -> append smaller.pop() -> to bigger half. 
                                -> bigger half [3], smaller half = [-1]
                    appending 4 -> append to smaller half -> [-4,-1]
                                -> pop from smaller half and append it to bigger half -> [3,4]
                                => bigger half is larger than smaller half -> smaller half = [-3,-1]/ bigger half = [4]
                    appending 5 -> appending to smaller half [-5,-3,-1]
                                -> appending to bigger half [4,5], smaller half = [-3,-1]
                    appending 2 -> sml = [-3,-2,-1]
                                -> bh = [3,4,5], sml = [-2,-1]
                                -> sml = [-3,-2,-1], bh = [4,5]
        -> median : sml.pop if len(sml) != len(bh)
           else:    (sml.pop + bh.pop)/2
                    
    '''
    def __init__(self):
        self.smaller_half = []
        self.bigger_half = []
    
    def push(self,val)-> None:
        smh = self.smaller_half 
        bgh = self.bigger_half 
        heapq.heappush(smh,-val)
        heapq.heappush(bgh,- heapq.heappop(smh))
        if len(smh) < len(bgh):
            heapq.heappush(smh,-heapq.heappop(bgh))
    
    def findMedian(self) -> float:
        if len(self.smaller_half) != len(self.bigger_half):
            return - heapq.heappop(self.smaller_half)
        else:
            return (- heapq.heappop(self.smaller_half) + heapq.heappop(self.bigger_half))/2


class TestFindMedian(unittest.TestCase):
    def setUp(self):
        self.solution = MedianFinder()
    def test_median(self):
        self.assertEqual( self.solution.smaller_half, [])
        self.assertEqual( self.solution.bigger_half,[])
        array = [3, 1, 4, 5, 2]
        median = 3 
        for num in array:
            self.solution.push(num)
        self.assertEqual(self.solution.findMedian(),median)
        print(f"Current array {array}, expected median {median}")
        array = [3,2, 1, 4, 5, 2]
        median = 2.5
        for num in array:
            self.solution.push(num)
        self.assertEqual(self.solution.findMedian(),median)
        print(f"Current array {array}, expected median {median}")


class MaximizeCapitalGained():
    def solution_one(self,k: int, w: int, profits: List[int], capital: List[int]):
        '''
        k = 2, w = 0, profits = [1,2,2,3,4], capital = [0,0,1,1,1]
        (1,1)
        (1,0),(2,1),(1,1),(4,1)
        heap = []
        visited = 

        create a tuple containing profits vs capital 
        while k >0:
            w = 0, 
            search for all projects that starts with 0 []
            -> put those projects into a heap [[-2,0],[-11,0]] max_heap
            -> put those projects into visited set() 
            -> pop the project [2,0] -> w = 2 
            -> used([2,0,1-index)]
            -> search for all other projects that have capital <=w and not in visited: 
            -> continue doing so until until k = 0. 
        return total profit 
        '''
        k = self.k 
        w = self.w
        profits = self.profits 
        capital = self.capital
        visited = set()
        heap = []
        while k > 0:
            for ind,val in enumerate(profits):
                capitalRequired = capital[ind]
                if capitalRequired <= w and ind not in visited:
                    visited.add(ind) 
                    heapq.heappush(heap, -val)
            if len(heap) == 0:
                return w
            biggestProfit = -(heapq.heappop(heap))
            w += biggestProfit
            k -=1 
        return w
    
    def solution_two(self,k: int, w: int, profits: List[int], capital: List[int]):
        '''
        Optimized approach:
        Create a list of tuples using projects/capitals
        Sort capitals first, as requirement. 

        Use a for loop for k:
            get all the project that has capital required satisfied. Instead of poping out or removing
            the project, we can keep them in the list and use a varible/pointer to see which 
            project we have already visited. 
            Push all those projects into a max_heap
            Check if max_heap's length is 0.
            If yes, break 
            Else:
                pop the value and add it to w:
        return w.
        '''
        projects = list(zip(capital,profits))
        projects.sort(key= lambda x: x[0])
        i = 0
        max_heap = []

        for _ in range(k):
            while i < len(projects) and projects[i][0] <= w:
                profit = projects[i][1]
                heapq.heappush(max_heap,-profit)
                i+=1
            if len(max_heap)== 0:
                break 
            w -= heapq.heappop(max_heap)
        return w

class TestMaximizeCapitalGained(unittest.TestCase):
    def setUp(self):
        self.solution = MaximizeCapitalGained()
    def test_maximizeCapitalGained(self):
        result = self.solution.solution_two(k=2,w=0,profits=[1,2,3],capital=[0,1,1])
        self.assertEqual(result,4)
        print(f"Test passed with expected result of result 4 vs actual result {result}")
        result = self.solution.solution_two(k=3,w=0,profits = [1,2,3],capital=[0,1,2])
        self.assertEqual(result,6)
        print(f"Test passed with expected result of result 6 vs actual result {result}")

def smallest_sum(nums1:List[int],nums2:List[int],k:int) -> List[List[int]]:
    '''
    So, the naive approach is to create a loop and find all the available pairs
    -> put them into a priority queue ( min heap)
    -> pop them out and return the list we needed. 

    => However, the time complexity is high. O(n*m* logn)

    We can improve this using similar approach.
    Initialize a heap = [] -> empty and 
    We start with the first element of nums1. -> pair it with all elements in nums2.
    Put them into a heap. 
    Afterwards, every time we pop element from the heap,
                sum, index1, index2 = heapq.heappop()
                -> check if index1 +1 < len(nums1):
    Example:    
    nums1 = [1,7,11], nums2 = [2,4,6], k = 5

            [1,2], [1,4],[1,6]
                |
        -> pop [0,0] -> [1,0] would be added -> [1,4],[1,6],[7,2]

        [1,2], [1,4],[1,6]
                |
        -> pop [0,1] -> [1,1] would be added -> [1,6],[7,2],[7,4]
        -> So basically, because the sorted arrays -> whenver we add new list, we add in the next possible smallest sum
    Because nums1 is sorted, the next larger element after nums1[i] is nums1[i+1]. So, once you pop (nums1[i], nums2[j]), you then check if i+1 is within bounds. If it is, you add the pair (nums1[i+1], nums2[j]) to the heap. This pair is the next candidate from the “column” corresponding to nums2[j].

        Why It Works:
        Since both arrays are sorted, when you replace nums1[i] with nums1[i+1] (while keeping the same nums2[j]), you get a pair that is guaranteed to be larger than (nums1[i], nums2[j]) but still small relative to other pairs. This way, you efficiently explore the next possible smallest pairs without having to consider every combination from scratch.
    '''
    heap = []
    for ind,val in enumerate(nums2):
        heapq.heappush(heap,(val+nums1[0],0,ind))
    ans = []
    while len(ans) < k:
        total_sum,ind1,ind2 = heapq.heappop(heap)
        ans.append([nums1[ind1],nums2[ind2]])
        if ind1 +1 < len(nums1):
            heapq.heappush(heap,(nums1[ind1+1]+nums2[ind2],ind1+1,ind2))
    return ans 

assert smallest_sum(nums1 = [1,7,11], nums2 = [2,4,6], k = 3) == [[1,2],[1,4],[1,6]]




        
if __name__ == "__main__":
    unittest.main()