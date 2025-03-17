'''
K-Messed Array Sort
Given an array of integers arr where each element is at most k places away from its sorted position, code an efficient function sortKMessedArray that sorts arr. For instance, for an input array of size 10 and k = 2, an element belonging to index 6 in the sorted array will be located at either index 4, 5, 6, 7 or 8 in the input array.

Analyze the time and space complexities of your solution.
2 5 8 3 
i = 3, curr = 3 
j = 2, 8 > 3 -> arr[3] = 8, j =1 -> 2 5 8 8 
j = 1, 5 > 3 -> arr[2] = 5, j = 0 -> 2 5 5 8
j = 0, 2 < 3 -> arr[1] = 3 -> 2 3 5 8

'''

class SortingSolution():

    def __init__(self, array, k):
        self.array = array 
        self.k = k
    def insertion_sort():
        array = self.array
        k = self.k 
        for i in range(len(arr)):
            curr = arr[i]
            j = i-1 
            while j >= max(0,i-k) and arr[j] > curr:
                arr[j+1] = arr[j]
                j-=1 
            arr[j+1] = curr 
        return array 
    

