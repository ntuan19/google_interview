'''
Unix system 
"." -> means in current directory
".." -> go back to prev directory 
"..." -> valid directory/file name 
"/" -> path must start with "/"
"//" -> ignore 
'''

class StackSolution():
    def simplifyPath(self,path:str)->str:
        '''
        Question 71: Simplify Path
        1. Use a stack to store valid directory names 
        2.Split the path by "/" to extract parts efficiently. 
        3. Process each components:
           - Ignore "" from consecutive slashes
           - Ignore ".", as it means "current directory"
           - ".." -> if the stack is empty 
                       -> do nothing because we are already at the root and cant go up further 
                  -> if the stack is not empty 
                       -> pop element from the stack because we need to go up one directory.
           - Another "..." -> treat it as normal 
        '''
        list_path = path.split("/")
        print(list_path)
        starting ="/"
        stack = []
        for component in list_path:
            if component == "" or component ==".":
                continue 
            elif component == "..":
                if not stack:
                    continue 
                else:
                    stack.pop()
            elif component == "...":
                stack.append("...")
            else:
                stack.append(component)
        while stack:
            starting += stack.pop(0) + "/"
        return starting[:-1] if len(starting)>1 else "/"
    
    def basicCalculator(s:str) -> int:
        '''
        FAANG
        '''
        stack = []
        total = 0 #Store the running total result 
        current_sign = 1 
        current_number = 0

        for char in s:
            if char.isdigit():
                current_number = current_number *10 + int(char)
            elif char == "+":
                total += current_sign * current_number
                current_sign = 1 
                current_number = 0 
            elif char =="-":
                total += current_sign * current_number
                current_sign = -1  # Set sign to negative
                current_number = 0
            elif char == "(":
                stack.append(total)
                stack.append(current_sign)
                total = 0 
                current_sign = 1 
            elif char == ")":
                total += current_sign * current_number
                total *= stack.pop()
                total += stack.pop()
                current_number = 0 
        
