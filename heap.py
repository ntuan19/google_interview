import heapq
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
        print(f"Current array {array}","expected median {median}")
        array = [3,2, 1, 4, 5, 2]
        median = 2.5
        for num in array:
            self.solution.push(num)
        self.assertEqual(self.solution.findMedian(),median)
        print(f"Current array {array}","expected median {median}")

if __name__ == "__main__":
    unittest.main()