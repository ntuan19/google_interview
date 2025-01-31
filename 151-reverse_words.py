
import unittest
# Helper function to reverse a portion of the string.
        
    
def swap(s, start, end):
            temp_start = start 
            temp_end = end 
            s_list = list(s)
            while start < end:
                s_list[start], s_list[end] = s_list[end], s_list[start]
                start += 1
                end -= 1 
            return "".join(s_list[temp_start:temp_end+1])

def reverseWords(s):
    '''
        my approach is to have two pointers
        i
        j 
        while i <= j < len(s):
                if i == " " and j == " ":
                    i+=1
                    j+=1 
                if i != " "  and j == " ":
                    swap values between i,j-1 
                    afterwards, 
                    update i equal to j
                else:
                    j+=1
        '''
    s = s[::-1]
    i = 0
    j = 0
    ans = ""
    while i <= j < len(s):
        if s[i] == " " and s[j] == " ":
            i+=1
            j+=1 
        elif s[i] !=" " and s[j] == " ":
            temp_i = i 
            temp_j = j -1
            ans += swap(s,temp_i,temp_j) + " "
            i =j 
        else:
            j+=1 
    if i < len(s):
        ans += swap(s,i,len(s)-1)
    return ans[:-1] if ans.endswith(" ") else ans 

def reverseWords2(s):
    words = s.split(" ")
    s = words
    s = [i for i in s if i]
    return " ".join(s[::-1])
        

class ReverseWordsConversion(unittest.TestCase):
    def test_example(self):
        self.assertEqual("world hello",reverseWords("  hello world  "))
        self.assertEqual("the sky is blue",reverseWords("blue is sky the"))
        self.assertEqual("the sky is blue",reverseWords2("blue is sky the"))
        self.assertEqual("world hello",reverseWords2("  hello world  "))





if __name__ == "__main__":
    unittest.main()

