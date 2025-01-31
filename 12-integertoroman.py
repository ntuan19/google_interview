'''

'''
import unittest
def intToRoman(num: int) -> str:
        ans = ""
        dic = {
            "M":1000,
            "CM":900,
            "D":500,
            "CD":400,
            "C":100,
            "XC":90,
            "L":50,
            "XL":40,
            "X":10,
            "IX":9,
            "V":5,
            "IV":4,
            "I":1
        }
        res = ""
        for symbol,val in dic.items():
            if num == 0:
                break  
            time,num = divmod(num, val) 
            res += symbol*time    
        return res 

class intToRoman(unittest.TestCase):
    def test_inttoRoman(self):
        self.assertEqual(intToRoman(3749),"MMMDCCXLIX")
        self.assertEqual(intToRoman(58),"LVIII")
        self.assertEqual(intToRoman(1994),"MCMXCIV")

