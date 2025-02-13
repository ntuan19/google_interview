'''
Longest common prefix
'''
from typing import List
from collections import deque 
class TrieNode():
    def __init__(self):
        self.children = {}
        self.count = 0 

class TriePrefix():
    def __init__(self,strs:List[str]):
        self.strs = strs
        self.root = TrieNode()

    def checkEmptyInput(self):
        if not self.strs:
            return ""

    def insert(self,word):
        node = self.root 
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode() 
            node = node.children[char]
            node.count +=1
    def createTrie(self):
        for word in self.strs:
            self.insert(word)
    
    def traverse(self):
        list_prefix = []
        node = self.root
        queue = deque([(node,"",0)])
        while queue:
            curNode, curr_str, freq = queue.popleft()
            for child in curNode.children:
                new_prefix = curr_str + child 
                freq = curNode.children[child].count 
                queue.append((curNode.children[child],new_prefix,freq))
                list_prefix.append((new_prefix,freq))
        return list_prefix         
    def findLongestCommonPrefix(self):
        node = self.root
        prefix = ""
        while node and len(node.children) ==1 and node.count == len(self.strs):
            char = list(node.children)[0]
            prefix += char
            node = node.children[char]
        print(prefix)
        return prefix 

prefixTrie = TriePrefix(["","f"])

prefixTrie.createTrie()
prefixTrie.traverse()
prefixTrie.findLongestCommonPrefix()