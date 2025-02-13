
import heapq
class Node():
    def __init__(self,val=0,next=None):
         self.val = val 
         self.next = next 
class LinkedList():
    def __init__(self,array):
        self.array = array
        self.head = None
    
    def create_linkedList(self):
        if not self.array:
            return None 
        self.head = Node(self.array[0])
        current_head = self.head
        for val in self.array[1:]:
            current_head.next = Node(val)
            current_head = current_head.next
        return self.head
    
    def reverse_linkedList(self):
        prev = None 
        current = self.head
        while current:
            next_node = current.next
            current.next = prev 
            prev = current
            current = next_node
        self.head = prev
        return prev

    def print_linkedList(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")
# Usage
linkedList = LinkedList([1, 2, 3, 4, 5])
linkedList.create_linkedList()

print("Original List:")
linkedList.print_linkedList()

linkedList.reverse_linkedList()

print("Reversed List:")
linkedList.print_linkedList()


'''
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

'''
class LLNode():
    def __init__(self,key = None,val = None):
        self.key = key 
        self.val = val

class HashMap():
    def __init__(self):
        self.head = None 
    
    def put(self,key,val):
        '''
        self.head is empty, then we put the first value in
        if the key is already in the node, we change the value 
        else, we go through the last node and put the key,val there
        '''
        if not self.head:
            self.head = LLNode(key=key,val=val)
        node = self.head 
        while node:
            if node.key == key:
                node.val = val 
                return 
            if not node.next:
                node.next = Node(key,val)
            node = node.next 
    def get(self,key):
        '''
        check if the key is in the list,
        if not, return -1 
        '''
        node = self.head
        while node:
            if node.key == key:
                return node.val 
            node = node.next 
        return -1 
    def remove(self,key):
        if not self.head:
            return 
        if self.head.key == key:
            self.head = self.head.next 
            return 
        prev = None 
        node = self.head
        while node:
            if node.key == key:
                prev.next = node.next 
                return 
            prev = node
            node = node.next 

def mergeKSortedLists(lists:List[Optional[Node]]):
    '''
    When there are multiple list and they are not sorted, what should we do in order to merge all the list together?
    The answer is consider using heapq.
    Min heap data structure basically compares element 
     (iterator1, iterator2, iterator3)
     -> minheap would check if iterator1 is similar compared to others in the heap
     -> if they are equal, they would use iterator2 
    '''
    minheap = []
    counter = 0
    for node in lists:
        if node:
            heapq.heappush(minheap,(node.val,counter,node))
    dummyNode = Node(float("inf"))
    head = dummyNode
    while minheap:
        node_val, currCounter, currNode = heapq.heappop(minheap)
        head.next = currNode 
        head = head.next 
        if currNode.next:
            counter+=1
            heapq.heappush(currNode.next.val,counter,currNode.next)
    return dummyNode.next 
    


    