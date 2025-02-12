'''
Palindrome number 
Given an integer x, return true if x is a 
palindrome
, and false otherwise.
U cant convert the number into string. 
'''

def isPalindrome(x: int) -> bool:
        '''
        so basically i am thinging of dividing the number 
        so that it would form sth like this 
        121 % 10 = 12 du 1 
        12%10 = 1 du 2 
        1 % 10 = 0 du 1 
        '''
        if x <0:
            return False 
        array = []
        while x > 0:
            x, remainder  = divmod(x, 10) 
            array.append(remainder)
        i = 0
        j = len(array)-1 
        while i<= j:
            if array[i] != array[j]:
                return False
            i+=1
            j-=1
        return True 

def plusOne(digits: List[int]) -> List[int]:
        addsOn = 0
        for i in range(len(digits)-1,-1,-1):
            if i != len(digits)-1 and addsOn == 0:
                return digits
            if i == len(digits)-1 and digits[i] +1 == 10:
                addsOn = 1 
                digits[i] = 0 
            elif i != len(digits) -1 and digits[i] + addsOn == 10:
                addsOn = 1 
                digits[i] = 0 
            else:
                digits[i]+=1
                addsOn = 0 
        if addsOn == 1:
            return [1]+ digits
        return digits

def trailingZeroes(n:int) -> int:
    total_zeroes = 0 
    k = 1 
    while n//(5**k) > 0:
        total_zeroes += n//(5**k)
        k+=1 
    return total_zeroes


def reverseInteger(x:int) -> int:
    INT_MAX = 2 **31 -1 
    result = 0 
    negative = False 
    if x < 0:
        x -= x*2
        negative = True
    while x !=0:
        digit = x%10 
        x = x /10 
        if (res == INT_MAX//10 and digit > 7) or (res > INT_MAX//10):
            return 0 
        res = res * 10 + digit 
    if negative:
        return - res 
    return res 



    

        
            
