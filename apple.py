'''
Given a string s, find the length of the longest 
substring
 without repeating characters.

 this is a sliding window problem.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:
dic = {}
i,j
   a b c a b c b b 
while i <=j:
    if j is not in dic:
        dic[word[j]] =1
        j +=1
        max_length = (j-i+1)
    else:
        dic[word[i]]-=1
        if dic[word[i]] == 0:
            del dic[word[i]]
return the max_length

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
"""

'''
import unittest
from collections import defaultdict
def longest_repeat_substrings(s):
    dic = defaultdict(int)
    i,j = 0,0
    max_length = 1
    for j in range(len(s)):
        if s[j] not in dic:
            dic[s[j]] =1 
            max_length = max(max_length,(j-i+1))
        else:
            while s[j] in dic and i <j:
                dic[s[i]]-=1
                i+=1
                if dic[s[i]] ==0:
                    del dic[s[i]]
            dic[s[j]] =1 
    return max_length 

# Test case class
class TestLongestSubstringWithoutRepeating(unittest.TestCase):
    def test(self):
        self.assertEqual(longest_repeat_substrings("abcabcbb"),3)
        self.assertEqual(longest_repeat_substrings("bbbbb"),1)
        self.assertEqual(longest_repeat_substrings("pwwkew"),3)



'''
// Whenever you expose a web service / api endpoint, you need to implement a rate limiter to prevent abuse of the service (DOS attacks).

// Implement a RateLimiter Class with an isAllowed() method.
 Every request comes in with a unique clientID. 
 Deny a request if that client has made more than N requests in the past T milliseconds.

class RateLimiter():


///
Key Components:
Dictionary for Clients:

Each client_id maps to a priority queue (min-heap).
The queue stores timestamps of valid requests in ascending order.
Priority Queue (Min-Heap):

Automatically maintains the oldest request timestamp at the top.
Ensures efficient removal of expired requests (O(log n)).
Logic for Handling Requests:

When a new request comes in:
Check the top of the queue. Remove timestamps that are outside the time window T (current_timestamp - top_of_queue > T).
If the queue length after cleanup is less than N (allowed requests), add the new request timestamp to the queue.
If the queue length is already N, reject the request.
'''

import time 
from collections import heapq
class RateLimiter():
    def __init__(self,max_requests, time_window):
        self.client_ids_requests = {}
        self.max_requests = max_requests
        self.time_window = time_window
    
    def isAllowed(self,client_request):
        client_id = client_request.headers.get('X-Client-ID')
        current_time_ms = int(time.time() * 1000)

        #initialize the clientId
        if client_id not in self.client_ids_requests:
            self.client_ids_requests[client_id] = deque()
        
        request_queue = self.client_ids_requests[client_id]
        while current_time_ms - self.client_ids_requests[client_id][0] > self.time_window:
                    request_queue.popleft()
            request_queue.append(allowed_time_ms)
        if len(self.current_ids_request[client_id]) <= self.max_requests:
                    return True 
                else:
                    return False 
        
    
# Run tests
if __name__ == "__main__":
    unittest.main()