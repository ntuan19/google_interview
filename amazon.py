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