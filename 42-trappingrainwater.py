def trap(height: List[int]) -> int:
        '''
        water can be trapped only by between the two taller walls.

        Height Array: [2, 0, 2]
            #       #
            #       #
            -----------
            2   0   2
        Water can be trapped at index 1, because it is between two taller bars.
        Step 2: Understanding How Water is Trapped
            Water at index 1 is limited by the shortest boundary of the two sides.
            The left max at index 1 is 2.
            The right max at index 1 is also 2.
            The amount of water trapped at index 1 is:
            scss
            Copy
            Edit
            min(left_max, right_max) - height[i] = min(2, 2) - 0 = 2

        Example
                  0 1 2 3 4 5 6 7 8 9 10 11
                 [0,1,0,2,1,0,1,3,2,1,2, 1]
             left 0 1 1 2 2 2 2 3 3 3 3  3 
            right 3 3 3 3 3 3 3 3 2 2 2  1
                    
            total = index1 -> min(0,3)- height[1] = 0
                    index2 -> min(1,3) - height[2] = 1 
                    index3 -> min(1,3) - height[3] = 0 
        '''
        left_maximum = -float("inf")
        dic_left = collections.defaultdict(int)
        for i in range(len(height)):
            left_maximum = max(height[i],left_maximum)
            dic_left[i] = left_maximum
        right_maximum = -float("inf")
        dic_right = collections.defaultdict(int) 
        for i in range(len(height)-1,-1,-1):
            right_maximum = max(height[i],right_maximum)
            dic_right[i] = right_maximum
        total = 0
        for i in range(1,len(height)-1):
            value= min(dic_left[i-1],dic_right[i+1]) - height[i]
            if value > 0:
                total += value  
        return total 
