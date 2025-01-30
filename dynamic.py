'''
Sinbad is out on the high seas, and he wants to maximize the distance he will travel. Sinbad has access to Google's weather API, so he knows how fast the winds will blow in the next N days,
which he writes down as an array A. If Sinbad works on day i, his ship will move forwards A[i] kilometres.

However, Sinbad doesn't like to work too hard for too long. Sinbad starts the trip at his energy capacity, K. A single day of work reduces it by 1. A single day of rest increases it by 1. 
With zero energy, Sinbad cannot work, and resting at full energy is possible but does nothing.

Example values:

N = 7
A = [10, 20, 0, 30, 5, 0, 10]
K = 3
We would like to write an algorithm that tells Sinbad on which days he should work, so as to maximize his distance traveled by the end of the trip. I want to learn how to solve this.How should i do this? 

 
    Day    0    1    2   3   4    5    6  
Energy 0   0    0    0   0   0    0    0
       1   10  []
       2
       3

energy if work: = max(dp[i-1][j+1] + A[i], dp[i][j])
energy if not work: = max(dp[i-1][j-1],dp[i][j])

'''


'''
Longest common subsequence.

      Str1   0   c     a      t
Str2   0     0   0     0      0
       c     
       r       
       a       
       b      
       t       
'''

