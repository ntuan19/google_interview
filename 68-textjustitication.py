'''
The idea is:
1. Create a function that can fit words into each line based on the maxWidth. 
        initilize an array line so we can append the word into it. 
        variable total to keep track of length of the line 
        keep track of the space between each word ( at least 1 space)
        line = []
        total = 0
        for word in all words:
            append the word into the an array line  
            #check if this length of the array is equal to maxWidth:
                   record the line into result array 
                   begin new line 
                   total = 0
            #if the length is more than waxWidth:
                   total = len(word)
                   record the previous line except current_word
                   line = [word]
            #if total < maxWidth and total >0:
                    total +=1 
2. Justify each line function
   -> Take care of how many spaces should be between each word,
   -> We care about even distribution of spaces, however, left is always prioritized in case of uneven distribution.
   -> We need to find out how many spaces left -> average space that can be evenly distributed among all words and the 
   rest of spaces that would be prioritized to the left sides.  
'''
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        ans = []
        def get_lines(words,maxWidth):
            line = []
            total = 0
            for word in words:
                total += len(word)
                line.append(word)
                if total == maxWidth:
                    total = 0 
                    lines.append(line[:])
                    line = []
                elif total > maxWidth:
                    total = len(word)
                    lines.append(line[:-1])
                    line = [word]
                if total < maxWidth and total >0:
                    total +=1 
            if len(line) != 0:
               lines.append(line)
        get_lines(words,maxWidth)

        def justify_line(line,last_line=False):
            new_line = ""
            total_words_length = sum(len(word) for word in line)
            if len(line) == 1:
                return line[0]+ " "*(maxWidth- len(line[0]))
            #check if this is the last_line.
            if last_line: 
                for i in range(len(line)):
                    if i != len(line)-1:
                       new_line += line[i]+ " "
                    else:
                        new_line += line[i] 
                        spaces_needed = maxWidth - len(new_line)
                        new_line += " "* spaces_needed 
                return new_line 
            
            spaces_left = maxWidth - total_words_length
            average_space = spaces_left// (len(line)-1)
            rest_space = spaces_left - (len(line)-1)*average_space
            #if this is not the last line 
            res_pace = collections.defaultdict(int)
            while rest_space >0:
                for ind,val in enumerate(line):
                    if rest_space > 0:
                       res_pace[ind] += 1 
                       rest_space -=1 
                    else:
                        break  
            for ind,val in enumerate(line):
                if ind == len(line)-1:
                    new_line +=val  
                    return new_line
                new_line += val + " "* average_space + " "*res_pace[ind]
            return new_line
        for i,line in enumerate(lines):
            if i == len(lines)-1:
                ans.append(justify_line(line,last_line=True))
            else:
                ans.append(justify_line(line))
        return ans 
            
                






                

                    

