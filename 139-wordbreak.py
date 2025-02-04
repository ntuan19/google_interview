'''
The problem of wordbreak:
given a string s and a list of strings WordDict, return true if s can be segmented into space-seperated sequence 
of one or more dictionary words

Two approach:
Approach A:
the first approach is to use BFS.
we start with index 0-i first.
We go through all possible ending indexes from 1 to n+1 (j)
    if s[i:j] in the wordSet:
     then append that ending to queue.
     if at any point, i == the end: then we know that the final word is found -> therefore,
     the string s can be segmented into space-seperated sequence.
    visited.add(i)

Approach B:

Another approach is create a 1D DP Array: dp

We have a for loop going through its ending index
   we have another for loop going through its starting index:
      we check if s[starting:ending] in wordset and dp[j] = True //meaning there is a word that can be segmented from s.
       dp[i] = True 
       break 
return dp[-1]
'''
import string 
from typing import List
from collections import deque 
import unittest 
class Solution:
    def __init__(self,s,wordDict:dict):
        self.s = s
        self.wordDict = wordDict
        self.length_s = len(s)
    def bfs_wordbreak(self):
        string = self.s
        wordSet = set(self.wordDict)
        queue = deque([0])
        visited = set()
        n = self.length_s
        while queue:
            start_ind = queue.popleft()
            for end_ind in range(start_ind+1,n+1):
                if string[start_ind:end_ind] in wordSet:
                    queue.append(end_ind)
                    if end_ind == n:
                        return True 
            visited.add(start_ind)
        return False 

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True  
        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True 
                    break  
        return dp[-1]

if __name__ == '__main__':
    def test_wordbreak(s: str, wordDict: List[str], expected: bool):
        sol = Solution(s, wordDict)
        result_bfs = sol.bfs_wordbreak()
        result_dp = sol.wordBreak(s, wordDict)
        print(f"Testing s: '{s}'")
        print(f"WordDict: {wordDict}")
        print(f"Expected: {expected}")
        print(f"BFS approach result: {result_bfs}")
        print(f"DP approach result: {result_dp}")
        print("-" * 40)
    
    # Test Case 1: Expect True ("leetcode" -> "leet code")
    test_wordbreak("leetcode", ["leet", "code"], True)
    
    # Test Case 2: Expect True ("applepenapple" -> "apple pen apple")
    test_wordbreak("applepenapple", ["apple", "pen"], True)
    
    # Test Case 3: Expect False (cannot form "catsandog" with the given dictionary)
    test_wordbreak("catsandog", ["cats", "dog", "sand", "and", "cat"], False)