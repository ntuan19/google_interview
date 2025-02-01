def distribute_candy(candies):
    '''
    The main solution is that we would consider two passes, focusing on the relationship between left and right side
    Firstly, we would have a pass from left to right, considering if the right value is larger than their left counterpart. If yes, we increment the value of 
    right value in the dictionary. 

    Similarly, we would have a pass from the right to the left. We would check if the maximum candies it have 
    '''
        dic = {n:1 for n in range(0,len(ratings))}
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                dic[i] = dic[i-1]+1
        n = len(ratings)
        for i in range(n-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                dic[i] = max(dic[i],dic[i+1]+1)
        return sum(val for val in dic.values())     
