'''
Design dynamic array 
'''
class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.array = []

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n 

    def pushback(self, n: int) -> None:
        # if self.capacity > len(self.array):
        #     self.array.append(n)
        # else:
        #     while self.capacity <= len(self.array):
        #         self.array.pop(0)
        #     self.array.append(n)
        if self.capacity == len(self.array):
            self.resize()
        self.array.append(n)

    def popback(self) -> int:
        return self.array.pop(-1)
 
    def resize(self) -> None:
        self.capacity += self.capacity

    def getSize(self) -> int:
        return len(self.array)
        
    def getCapacity(self) -> int:
        return self.capacity