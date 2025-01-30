'''
 Two pointers is used for searching pairs in a sorted array, 
 For instance, we can utilise two pointers to find the sum of two numbers in a sorted array.
'''

def two_sum(numbers, target):
    #ensure the numbers is sorted array 
    left, right = 0, len(numbers) - 1
    while left < right:
        if numbers[left] + numbers[right] == target:
            return 1 
        elif numbers[left] + numbers[right] < target:
            left +=1 
        else:
            right-=1
    return 0 

'''
However, sometimes the input is not sorted and if use sorting, time complexity would be O(nlogn) rather than O(n). 
Still, some applications for two pointers.
1. The first application is partition the array ( especially around a pivot)
Imaging having a list of numbers, and a pivot. You have to partition the array and ensures that all numbers to the left of the 
pointer is less than the pivot and all numbers to the right of the pivot is larger or equal to the pivot itself

Example: [-23,43,44,2,4,34,23,65,18], pivot = 34
'''

def partition_array(numbers,pivot):
    left = 0
    right = len(numbers) -1 
    while left <= right:
        if numbers[left] <= pivot <= numbers[right]:
            left +=1
            right -=1
        elif numbers[left] > pivot and numbers[right] < pivot:
            numbers[left],numbers[right] = numbers[right], numbers[left]
            left +=1
            right -=1
        elif numbers[left] > pivot and numbers[right] > pivot:
            right -=1
        elif  numbers[left] < pivot and numbers[right] < pivot:
            left +=1
    return numbers
# print(partition_array([-23,43,44,2,4,34,23,65,18],34))
#Another way to write the code 
def partition_array_approach(numbers,pivot):
    left = 0
    right = len(numbers) -1 
    while left <= right:
        if numbers[left] <= pivot:
            left+=1
        elif numbers[right] >= pivot:
            right -=1
        else:
            numbers[left], numbers[right] = numbers[right],numbers[left]
            left +=1
            right -=1
    return numbers
# print(partition_array_approach([-23,43,44,2,4,34,23,65,18],34))


'''
Segregating Elements
Example 1: Separating even and odd numbers
Let’s say we want to rearrange an array so that all even numbers come before all odd numbers. The array doesn't need to be sorted, just segregated.
'''
def segregate_array(numbers):
    left = 0
    right = len(numbers) -1 
    while left <= right:
        if numbers[left] %2 == 0:
            left +=1 
        elif numbers[right] %2 != 0:
            right -=1
        else:
            numbers[left], numbers[right] = numbers[right], numbers[left]
            left+=1
            right-=1
    return numbers
# print(segregate_array([-23,43,44,2,4,34,23,65,18]))

'''
To conclude: the code is basically similar to both segregate array/ or partition the array. 
Partition the array based on pivot
Segregate the array based on certain condition. 
'''

'''
Sliding window using two pointers
Sliding window is basically used to efficiently find subarrays/substrings that meet certain criteria, without having to repeatedly process the entire aray 
This method involves maintaining a window (a range of elements) and expanding or contracting that window by moving two pointers—left and right—to cover different sections of the array.
Let's dive into the first use case. 
Finding the sum of a subarray of a given size.
Example 1: Find the maximum sum of a subarray of size k
Given an array and a number k, find the maximum sum of any subarray of size k.

Example 2: Find the smallest subarray with a sum greater than or equal to a target
Given an array of positive integers and a target sum, find the length of the smallest subarray whose sum is greater than or equal to the target.

nums = [2, 1, 5, 2, 3, 2]
target = 7 

l = 0
sum = 0
sum += nums[l]
r = 1
min_length = float(inf)
while l <=r< len(nums):  
    while sum < target:
        sum += nums[r]
        r +=1
    while sum >= target:
        min_length = min(r-l,min_length)
        sum -= nums[l]
        l +=1
return min_length

0 < 1 < 6 -> sum = 2 < 7 -> sum = 3, r = 2
          -> sum = 3 < 7 -> sum = 8, r = 3
          -> sum = 8 > 7 -> min_length = (3-0) = 3 -> sum -2 = 6 , l = 1

1 < 3 < 6 -> sum = 6 < 7 -> sum += 2  = 8, r = 4
          -> sum > = target -> min_length = 3, sum = 7, l = 2
          -> sum = 7 = target -> min_length = (4-2) = 2
          -> 

'''
def find_smallest_subarray_sum(nums,target):
    l = 0
    total = 0
    total += nums[l]
    r = 1
    min_length = float('inf')
    if total >= target:
        return 1
    while l <=r< len(nums):  
        while total < target and r < len(nums):
            total += nums[r]
            r +=1
        while total >= target:
            min_length = min(r-l,min_length)
            total -= nums[l]
            l +=1
    return min_length if min_length != float('inf') else 0

# find_smallest_subarray_sum([2,1, 5, 2, 3, 2], 1000)


'''
So the approach here is we want to go through the entire list and sum the values up. 
However, because we want to know which is the smallest subarray, so we compact/ expand the window of two pointers as long as 
the sum is larger or equal to the target. 
'''
def find_smallest_subarray_sum_2(nums,target):
    l = 0 
    total = 0
    min_length = float('inf')
    for i in range(len(nums)):
        total += nums[i]
        while total >= target:
            min_length = min(min_length, i -l+1)
            total -= nums[l]
            l +=1 
    return min_length

'''
Another problem is to find the longest subarray without repeating characters. 
Example: abcabcbb
# Expected output: 3
'''

def find_longest_subarray(string_input):
    original_set = ''
    l = 0 
    longest_subarray = 0
    for i in range(len(string_input)):
        if string_input[i] not in original_set:
            original_set += string_input[i]
            longest_subarray = max(longest_subarray, len(original_set))
        else:
            while string_input[i] in original_set:
                  original_set = original_set[1:]
    return longest_subarray
# print(find_longest_subarray('abcabcbb'))


'''
Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
This is an important part because of the logic.
So after we sort the array, we can use two pointers technique. 


So once we find the triplets, like example curr [i] + nums[left] + nums[right] < target, 
-> it means that all the numbers between left and right will satisfy the condition as well. 
-> so we can add the count of the triplets by the number of elements between left and right = count += (right-left)
-> then we move the left pointer to the right to find other possible triplets ( increase left to find other possible triplets)
'''
def find_number_of_triplets(nums,target):
    nums.sort()
    count = 0
    for i in range(len(nums)):
        left = i+1
        right = len(nums) -1
        while left < right:
            triplet_sum = nums[i] + nums[left] + nums[right]
            if triplet_sum < target:
                count+= (right-left)
                left+=1
            else:
                right -=1
    return count

print(find_number_of_triplets([-2,0,1,3],2) == 2)
print(find_number_of_triplets([3,1,0,-2],4) == 3)


'''

Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

what we can do is 
[10,50,100,600]
add one at the begininng of the list of numbers => [1,10,50,100,600]
initilize the value count = 0
l = 0
r = 1 
while l < r < len(product):
    while product[r]/product[l] < target:
        r +=1
    count+= (r-l-1)
    l +=1
return count 


'''
# def countContinuousSubarrays(nums,target):
#     val = 1
#     product = []
#     for i in range(len(nums)):
#         val = val * nums[i]
#         product.append(val)
#     l = 0
#     r = 1 
#     count = 0
#     product = [1] + product
#     while l < r < len(product):
#         while product[r]/product[l] < target and l < r< len(product):
#             r +=1
#         count+= (r-l-1)
#         l +=1
#     return count 

# assert (countContinuousSubarrays([10,5,2,6],100)) == 8
# assert (countContinuousSubarrays([1,2,3,4,5],100)) == 13


'''
Given an integer array nums and an integer k, return the maximum length of a 
subarray that sums to k. If there is not one, return 0 instead.


'''



'''
For this problem, your goal is to sort an array of 0, 1 and 2's but you must do this in place, in linear time
and without any extra space (such as creating an extra array). 
This is called the Dutch national flag sorting problem.
For example, if the input array is [2,0,0,1,2,1] then your program should output [0,0,1,1,2,2] and
the algorithm should run in O(n) time.

[2,0,0,1,2,1]
l = 0
r = 5
m = 1
for i in range(l+1,r):
    if m 

The algorithm needs to run in O(n): time complexity. You have to sort this in-place, no additional space is allowed. 
'''

def dutchFlagProblem(nums):
    l = 0 
    r = len(nums)-1
    m = 0
    while m <= r:
        if nums[m] == 0:
            nums[l],nums[m] = nums[m], nums[l]
            m+=1
            l +=1
        elif nums[m] == 2:
            nums[r],nums[m] = nums[m], nums[r]
            r -=1
        else:
            m+=1
    return nums

print(dutchFlagProblem([2,0,2,2,2,2,1,1,1,1,0,0,2,2,1]))

# [2,0,0,1,2,1]

def findShortestLength(nums):
    l = 0
    r = len(nums)-1
    arr = []
    while l < r:
        min_val = min(nums[l:])
        max_val = max(nums[:r+1])
        min_indx = nums.index(min_val)
        max_indx = nums.index(max_val)
        if min_indx == l and max_indx == r:
                    l+=1
                    r-=1
        else:
            return nums[l:r+1]     
    return []


            