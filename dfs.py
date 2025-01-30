# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Build the tree:
#       1
#      / \
#     2   3
#    / \   \
#   4   5   7
#  /     \
# 6       9
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(7)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(6)
root.left.right = TreeNode(5)
root.left.right.right = TreeNode(9)


# Test array
arr1 = [1, 2, 3,4]
arr2 = [1,2,5,6]
arr3 = [1,2,4,7]
arr4 = [1,2,4,6]
arr5 = [1,2,5,6]
arr6 = [2,5,9,10]
arr7 = [1,2,5,9]
arr8 = [1,3,7]



def isValidSequence(root,arr):
    def traverse(node,level,arr):
        if not node:
            return False
        if level >= len(arr) or node.val != arr[level]:
            return False 
        if not node.left and not node.right:
                return True
        return traverse(node.left,level+1,arr) or traverse(node.right,level+1,arr)
    return traverse(root,0,arr)
        
# Check if the array is a valid sequence
print(isValidSequence(root, arr1))  # Output: False
print(isValidSequence(root, arr2))  # Output: False 
print(isValidSequence(root, arr3))  # Output: False 
print(isValidSequence(root, arr4))  # Output: True
print(isValidSequence(root, arr5))  # Output: False 
print(isValidSequence(root, arr6))  # Output: False 
print(isValidSequence(root, arr7))  # Output: True
print(isValidSequence(root, arr8))  # Output: True


