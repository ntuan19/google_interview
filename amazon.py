'''
A team of financial analysts at amazon has designed a stock indicator to determine the consistency of amazon's stock in delivery returns daily. 
More formally, the percentage return (rounded off to nearest integer) delivered by the stock each day over the last n days is considered. 
This is given as an array of integers, stockPrices. The stock's k-consistency score is calculated using the following operations:

In a single operation, omit a particular day's return from stockPrices array to get have one les element, then rejoin the parts of the array.
 This can be done at most k times.
The maximum number of contiguous days during which the daily return was the same is defined as the k-consistency score for amazon's stock. 
Note that the return may be positive or negative.
As part of the team, you have been assigned to determine the k-consistency score for the stock.
 You are given an array stockPrices of size n representing the daily percentage return delivered by amazon stock and a parameter k.


Determine the k-consistency score.


Example:
stockPrices = [1, 1, 2, 1, 2, 1]
k = 3


After omitting the integers at 3rd and 5th positions, the array is [1, 1, 1, 1]. It is better not to do the remaining allowable operation.
The longest set of contiguous period with the same percentage return is [1, 1, 1, 1]. The k-consistency score is its length, return 4.


Code : The idea is to use sliding Window or dp.
'''


'''
You are given a class LongestConsecutiveSequence which exposes a function addNumberAndCompute that accepts a number as an argument.
This function can be called by the client any number of times as per their liking. After each computation the function is supposed
to return the length of the longest consecutive sequence you have seen till now.
Initially i struggled with the question and was not able to understant it properly then he explained me the question and pasted the few testcases.
addNumberAndCompute(1), returns 1
addNumberAndCompute(2), returns 2
addNumberAndCompute(4), returns 2
addNumberAndCompute(3), return 4

{1:1, 2:2, 4:4,3:3}
'''
from collections import defaultdict
class LongestConsecutiveSequence():
    def __init__(self):
        self.dic = defaultdict(int)
        self.max_length = 0 
    def addNumberAndCompute(self,number:int):
        if number in self.dic:
            return self.max_length 
        left_side = self.dic.get(number-1,0)
        right_side =self.dic.get(number+1,0)
        current_length = left_side +right_side+1 
        self.dic[number] = current_length 

        self.dic[number-left_side] = current_length 
        self.dic[number+right_side] = current_length
        self.max_length = max(self.max_length, current_length)
        return self.max_length 

lcs = LongestConsecutiveSequence()
# print(lcs.addNumberAndCompute(1))  # Expected output: 1
# print(lcs.addNumberAndCompute(2))  # Expected output: 2
# print(lcs.addNumberAndCompute(4))  # Expected output: 2
# print(lcs.addNumberAndCompute(3))  # Expected output: 4


'''
1. Permission Evaluator
Problem Statement:
You are given three inputs:

A dictionary mapping user IDs to a list of role IDs (e.g., { "alice": ["admin", "editor"], "bob": ["viewer"] }).
A dictionary mapping role IDs to a list of permissions (e.g., { "admin": ["read", "write", "delete"], "editor": ["read", "write"], "viewer": ["read"] }).
A dictionary representing role inheritance, where a role can inherit permissions from other roles (e.g., { "admin": ["editor"], "editor": [] }).
Implement a function that checks if a given user has a specific permission. The function should account for direct permissions from the user’s roles and permissions inherited through role hierarchies.

Example:

Input:

user_roles = { "alice": ["admin", "editor"], "bob": ["viewer"] }
role_permissions = { "admin": ["read", "write", "delete"], "editor": ["read", "write"], "viewer": ["read"] }
role_inheritance = { "admin": ["editor"], "editor": [] }
Query: Does alice have the "delete" permission?
Output:

True (because "alice" directly gets "delete" from the "admin" role)
'''

'''
. Login Rate Limiter
Problem Statement:
Given a stream (or list) of login events represented by a tuple (user, timestamp, status)—where status can be "success" or "fail"—
implement a function that detects if any user exceeds N failed login attempts within a 5-minute (300-second) window.
 Return a list of users (or alert events) that meet this threshold.

Example:

Input:

events = [("alice", 100, "fail"), ("alice", 200, "fail"), ("alice", 250, "fail"), ("bob", 300, "fail"), ("alice", 310, "fail")]
N = 3
Output:

["alice"]
(Alice had 4 failed attempts between time 100 and 310, which exceeds the threshold within 300 seconds.)
Hint:
Use a sliding window technique to maintain a count of failed login attempts for each user over the last 300 seconds. A dictionary can be used to map users to a queue or list of timestamps for their failed attempts.



'''

'''
Session Duration Analyzer 

Alice wants to track the time logged in/logged out.

'''
def calculate_session_durations(events):
    # Sort events by timestamp (the third element in each tuple)
    events.sort(key=lambda x: x[2])
    
    status = {}       # status[user] = True if user is logged in, else False
    login_times = {}  # login_times[user] = login timestamp
    total = {}        # total[user] = accumulated session duration
    
    for user, action, timestamp in events:
        if action == "login":
            # If the user is already logged in, we could ignore duplicate logins,
            # or update to the new timestamp if needed. Here, we ignore if already logged in.
            if not status.get(user, False):
                status[user] = True
                login_times[user] = timestamp
            # else: Ignore the login since the user is already logged in
        elif action == "logout":
            # Only process logout if the user was marked as logged in
            if status.get(user, False):
                # Calculate session duration and add to total
                session_duration = timestamp - login_times[user]
                total[user] = total.get(user, 0) + session_duration
                status[user] = False  # mark user as logged out
            # If logout comes with no prior login, ignore it as invalid data.
    
    return total

# Example usage:
events = [
    ("alice", "login", 100),
    ("alice", "login", 400),
    ("alice", "logout", 500),
    ("alice", "logout", 200),
    ("bob", "logout", 40),
    ("bob", "logout", 300),
    ("bob", "login", 150)
]

#print(calculate_session_durations(events))



'''
Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""

'''
from collections import Counter
import heapq

def reorganizeString(s: str) -> str:
        '''
        dic = {a:1,b:1}
        choose letter with the most freq
        a -> choose another letter with highest frequency. 
        b -> 
        heap = []
        '''

        max_heap = []
        dic = Counter(s)
        for char, count in dic.items():
            heapq.heappush(max_heap, (-count,char)) 
        new_s = ""
        while max_heap:   #((-2,a),(-1,b)),
            freq,char = heapq.heappop(max_heap) #-2,a 
            if new_s and new_s[-1] == char: 
                if max_heap:
                        newfreq,newchar = heapq.heappop(max_heap)
                        new_s += newchar
                        if newfreq+1 <= -1:
                            heapq.heappush(max_heap,(newfreq+1,newchar))
                else:
                    return ""
                if freq <= -1:
                    heapq.heappush(max_heap,(freq,char))
            else:
                new_s += char 
                if freq +1 <= -1:   #
                        heapq.heappush(max_heap,(freq+1,char))
        return new_s
print(reorganizeString("aab"))

class Solution:
    def ladderLength(self, start_word: str, end_word: str, words: List[str]) -> int:
        '''
        get all the words into a set.
        create an adjancy list to keep trck of words that differ by one char. 
        do a bfs to see which is the shortst path to get to the endword.
        '''
        dic = defaultdict(set)
        setWords = set(words)
        setWords.add(start_word)
        alphabet = "qwertyuiopasdfghjklzxcvbnm"
        for word in setWords:
            for i in range(len(word)):
                for char in alphabet:
                    newW = word[:i] + char+ word[i+1:]
                    if newW != word and newW in setWords:
                        dic[word].add(newW)
                        dic[newW].add(word)
        visited = set()
        queue = deque([(start_word,1)])
        visited.add(start_word)
        if start_word not in dic:
            return 0 
        while queue:
            currW, time = queue.popleft()
            if currW == end_word:
                return time 
            if dic[currW]:
                for word in dic[currW]:
                    if word not in visited:
                        queue.append((word,time+1))
                        visited.add(word)
        return 0 

