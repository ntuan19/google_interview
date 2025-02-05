'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.
Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
'''


def lengthOfSequence(nums):
        '''
        10,    9,   2,   5,    3,   7,    101,    18
        0.     0.   0.   1.    1.   2      3.     3 
        Checking the values before nums[i]
        '''
        dp = [0 for _ in range(len(nums))]
        for i in range(1,len(nums)):
            for j in range(i):
                #check any 
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
        res = max(dp) 
        return res +1 

