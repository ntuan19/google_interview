'''
Diameter of a binary tree 
Given a tree, what can we do to calculate its diameter.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
Generally what we can do is 
1. check for base case,if the node is empty, then the value of diameter is 0.
2. calculate the left length and the right length
3. calculate the diameter 
We have to return the maximum_length of either left side or right side. 
'''
from typing import Optional 

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val 
        self.left = left 
        self.right = right 

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0 
        def depth(node:Optional[TreeNode()])-> int: 
            if not node:
                return 0 
            left = depth(node.left)
            right = depth(node.right)
            self.diameter = max(left +right,self.diameter)
            return  1+ max(left,right)
        depth(root) 
        return self.diameter


        '''

        Similarly, we can apply the same logic to calculate the diameter of N-Ary Tree
        '''
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        diameter = 0 
        def depth(node):
            nonlocal diameter
            if not node:
                return 0 
            max_height = []
            if node.children:
               for child in node.children:
                max_height.append(depth(child))
            # Ensure we have at least two values for max_height:
            if len(max_height) == 0:
                first = second = 0
            elif len(max_height) == 1:
                first = max_height[0]
                second = 0
            else:
                max_height.sort(reverse=True)
                first = max_height[0]
                second = max_height[1]
            diameter = max(first+second,diameter)
            return 1 + first
        depth(root)
        return diameter


        '''
        Invert a Binary Tree

        '''
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        root.left, root.right = root.right,root.left 
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        
        '''
        Binary Tree Maximum Path Sum 
        The core idea here is recursively calculate the value of the left side/right right 
        if the left_side, right_side is smaller than 0, then we prune that subtree -> use max(left_side,0) -> always ensure we have 0 as minimum.
        total here is to calculate the cumulative sum from both left/right sides
        
        '''
    def maxPathSum(self,root:Optional[TreeNode]):
        total = -float("inf")

        def calculate_path(node):
            if not node:
                return 0 
            left_side = max(calculate_path(node.left),0)
            right_side = max(calculate_path(node.right),0)
            total = max(total, node.val + left_side + right_side)
            return node.val + max(left_side,right_side)
        calculate_path(root)
        return total 