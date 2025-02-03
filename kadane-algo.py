'''
Question 53 
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        max_sum = -float("inf")
        for num in nums:
            total+= num 
            max_sum = max(max_sum,total) 
            if total <0:
                total = 0 
        return max_sum
        
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        '''
        '''
        maximum_subarray = -float("inf")
        minimum_subarray = float("inf")
        total = 0
        total_min = 0
        total_sum = sum(nums)
        for num in nums:
            total += num   
            total_min += num 
            maximum_subarray = max(maximum_subarray,total)
            minimum_subarray = min(minimum_subarray,total_min)
            if total <0:
                total = 0 
            if total_min >0:
                total_min =0 
        if maximum_subarray <0:
            return maximum_subarray
        return max(maximum_subarray,total_sum-minimum_subarray)




