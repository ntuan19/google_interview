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
from typing import Optional, List

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
    def diameterOfNAryTree(self, root: 'Node') -> int:
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
    
    def right_side_view(self,root:Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        ans = []
        while queue:
            queue_length = len(queue)
            for i in range(queue_length):
                node = queue.popleft()
                if i == queue_length - 1:
                    ans.append(node.val)  
                if node.left != None:
                    queue.append(node.left) 
                if node.right != None:
                    queue.append(node.right) 
        return ans  

        def zigzagLevelOrder(self,root:Optional[TreeNode]) -> List[List[int]]:
            '''
            so the core idea here is that you need to know how many nodes are there on each level.
            Usually the first level is always a root node -> so u know that it is 1.
            So, u keep track of the number of nodes on the first level. 
            You can still add more nodes to the queue. 

            '''
            levels = []
            if not root:
                return []
            def helper(root, level):
                queue = deque([root])
                left_to_right = True
                while queue:
                    number_of_nodes_on_level = len(queue)
                    list_of_nodes = deque()
                    for _ in range(number_of_nodes_on_level):
                        node = queue.popleft()
                        if left_to_right:
                            list_of_nodes.append(node.val)
                        else:
                            list_of_nodes.appendleft(node.val)
                        if node.left:
                            queue.append(node.left)
                        if node.right:
                            queue.append(node.right)
                    left_to_right = not left_to_right
                    levels.append(list(list_of_nodes))
            helper(root,0)
            return levels


class BinaryTree_Iterator():
    '''
    Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

    BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
    boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
    int next() Moves the pointer to the right, then returns the number at the pointer.
    Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

    You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

       7
      / \
     3   15
         / \
        9   20
        How the Stack is Built and Used
    Initialization:

    We start at the root node (7).
    We push 7 onto the stack.
    Then we move to the left child of 7, which is 3, and push 3 onto the stack.
    Stack now: [7, 3]
    (Remember, the rightmost element in our list represents the top of the stack, so 3 is on top.)
    First Call to next():

    We call next(), which pops the top element from the stack.
    Popped Element: 3
    Since 3 does not have a right child, nothing additional is added to the stack.
    Stack remains: [7]
    Output: 3
    Second Call to next():

    Next, we call next() again.
    This time, the top element on the stack is 7, so we pop 7.
    Popped Element: 7
    Now, we check if 7 has a right child. It does: node 15.
    Since 7 has a right child, we push all the left children of 15 onto the stack:
    First, we push 15.
    Then we move to the left child of 15, which is 9, and push 9.
    Stack now becomes: [15, 9]
    (Again, 9 is on top because it’s the leftmost node in the subtree rooted at 15.)
    Output: 7
    Next Calls:

    On the next call to next(), we pop 9 (the top of the stack). Since 9 has no right child, nothing is added.
    Stack becomes: [15]
    Output: 9
    Then, calling next() again pops 15.
    Since 15 has a right child (20), we push 20 and any left children of 20 (in this case, 20 has no left child).
    Stack becomes: [20]
    Output: 15
    Finally, calling next() pops 20.
    20 has no right child.
    Stack becomes: []
    Output: 20
    Key Point
    You only add nodes to the stack when the node you just popped has a right child.

    When you pop a node (like 7), if it has a right child (like 15), you then push that right child and all of its left descendants (in this case, 9) onto the stack.
    This ensures that the smallest unvisited node is always on top of the stack.
    Summary
    Initially: Stack is built by pushing all left children from the root: [7, 3].
    First next() call: Pops 3 (no right child, so nothing added).
    Second next() call: Pops 7; since 7 has a right child (15), push 15 and then its left child 9 → Stack becomes [15, 9].
    Subsequent calls: Continue this process, always ensuring that when a node with a right child is popped, you push its right child and the entire left branch of that child.

    '''
    def __init__(self,root:TreeNode):
        self.stack = []
        self.push_all_left_element()
    
    def push_all_left_element(self,node: TreeNode):
        while node:
            stack.append(node)
            node = node.left 
    
    def next(self) -> int:
        '''
        Moves the pointer to the right in the in-order traversal and returns the number at the pointer.
        '''
        current_node = self.stack.pop() 
        if current_node.right:
            self.push_all_left_element(current_node.right)
        return current_node
    
    def hasNext(self) -> bool:
        return len(self.stack) >0
    


