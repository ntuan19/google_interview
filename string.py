'''
longest substring without repeating character
What we can do is we initialize a loop going through the whole string.We have another pointer from the beginning 
i,j= 0,0 
At the same time, we keep track of the number of characters that are in the window.
'''
from collections import defaultdict
def lengthOfLongestSubstring(s:str) -> int:
    i = 0 
    dic = defaultdict(int) 
    max_length = 0
    for j in range(len(s)):
        dic[s[j]]+=1
        while s[j] in dic and dic[s[j]] >1:
            dic[s[i]]-=1
            i+=1
        max_length = max(j-i+1, max_length)
    return max_length 

assert(lengthOfLongestSubstring("aba")==2)
assert(lengthOfLongestSubstring("abded")==4)



'''
Longest Palindrome Substring 
Given a string s, return the longest palindromic substring in s.

longestSubstring = "" -> use max(key= len) to compare
we have a function to check if the substring is a palindrome. 
     - take in start, end as input 
     - if 0<=start and end <= len(s) and start == end:
           then start-=1, end +=1 
           else:
            return the string. 
'''
def checkPalindrome(s,start,end):
        if s[start] != s[end]:
            return ""
        while 0 <= start-1 and end+1 <len(s):
            if s[start-1] == s[end+1]:
               start-=1 
               end +=1
            else:
                return s[start:end+1]
        return s[start:end+1]
# print(checkPalindrome("aba",1,1))
# print(checkPalindrome("abba",1,2))
# print(checkPalindrome("abbbac",2,3))
# print(checkPalindrome("abbbbad",2,3))
# print(checkPalindrome("dbbbbak",2,3))
# print(checkPalindrome("dabaabkdk",2,2))




def longestPalindromicSubstring(s:str) -> str:
    longestSubstring = ""
    def checkPalindrome(start,end):
        if s[start] != s[end]:
            return ""
        while 0 <= start-1 and end+1 <len(s):
            if s[start-1] == s[end+1]:
               start-=1 
               end +=1
            else:
                return s[start:end+1]
        return s[start:end+1]
    
    for i in range(len(s)):
        longestSubstring = max(checkPalindrome(i,i),longestSubstring, key = len)
    for i in range(len(s)-1):
        longestSubstring = max(checkPalindrome(i,i+1),longestSubstring, key = len)
    return longestSubstring
assert (longestPalindromicSubstring("babad") == "aba")
assert (longestPalindromicSubstring("cbbd") == "bb")

'''


'''
def longestPalindromeSubstringDP(s:str)->str:
        n = len(s) 
        if n == 0:
            return ""
        dp =[[False]*n for i in range(n)]
        start,max_len = 0,1 
        #Every single character is a palindrome 
        for i in range(n):
            dp[i][i] = True  
        
        #check for two character substrings
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True 
                start, max_len = i,2
        # Expand for substrings of length 3 or more
        for length in range(3, n + 1):  # Length of substring
            for i in range(n - length + 1):
                j = i + length - 1  # Ending index
                if s[i] == s[j] and dp[i + 1][j - 1]:  # Expand from the center
                    dp[i][j] = True
                    start, max_len = i, length

        return s[start:start + max_len]


