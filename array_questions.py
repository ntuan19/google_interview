'''
Zigzag conversion
In question, we need to convert the string in zig-zag pattern i.e. think we have 2D array with row n and no limit of column and write the given string in this format

First go from top to down writing each character, then go to next column but one above row until you reach top row. And follow this pattern repeatedly.
Pattern (row = 5)

1                  9                      17
2             8    10               16   18                24
3       7          11         15         19          23 
4   6              12   14               20    22
5                 13                    21

To do this problem:


we can see the pattern:
1. For the first row/last row to reach its next value in its row:
    it takes (n-1)*2 jumps

2. For other rows to reach its values, 
   it takes (n-1)*2 - r *2 

'''
import unittest

def zigzag_conversion(s,numRows):
    #changing comments
    res = []
    def find_values(row_index):
                values_index = []
                total = row_index
                while total < len(s):
                    values_index.append(s[total])
                    second_total = total + 2*(numRows-1) - 2*(row_index)
                    if second_total < len(s) and row_index != 0 and row_index != numRows-1:
                        values_index.append(s[second_total])
                    total += 2 *(numRows-1)
                return values_index
    #fill the first column
    for ind in range(numRows):
        values_index = find_values(ind)
        res.append(values_index)
    return "".join(char for sublist in res for char in sublist)


class TestZigzagConversion(unittest.TestCase):
    def test_example(self):
        self.assertEqual("PAHNAPLSIIGYIR", zigzag_conversion("PAYPALISHIRING", 3))
        self.assertEqual("PINALSIGYAHRPI", zigzag_conversion("PAYPALISHIRING", 4))
        self.assertEqual("A", zigzag_conversion("A", 1))

if __name__ == "__main__":
    unittest.main()

