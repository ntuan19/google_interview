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