# Given pre-order and in-order traversals of a binary tree, write a function 
# to reconstruct the tree.
# For example, given the following preorder traversal:
# [a, b, d, e, c, f, g]
# And the following inorder traversal:
# [d, b, e, a, f, c, g]
# You should return the following tree:
#     a
#    / \
#   b   c
#  / \ / \
# d  e f  g

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def create_tree(arr):
    global preorder_index
    index = None
    preorder_index += 1
    
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return Node(arr[0])
    
    parent = preorder[preorder_index]
    for i in range(len(arr)):
        if arr[i] == parent:
            index = i
    left = arr[:index]
    right = arr[index+1:]
    
    left = create_tree(left)
    right = create_tree(right)
    return create_node(arr[index], left, right)

def create_node(val, left, right):    
    node = None    
    if left == None:
        node = Node(val)
    else:
        node = Node(val, left, right)
    return node

preorder = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
inorder = ['d', 'b', 'e', 'a', 'f', 'c', 'g']
preorder_index = -1

root = create_tree(inorder)

#################### TESTING ####################
# code from GeeksforGeeks

def printInorder(root): 
  
    if root: 
  
        # First recur on left child 
        printInorder(root.left) 
  
        # then print the data of node 
        print(root.val, end=" "), 
  
        # now recur on right child 
        printInorder(root.right) 
        
def printPreorder(root): 
  
    if root: 
  
        # First print the data of node 
        print(root.val, end=" "), 
  
        # Then recur on left child 
        printPreorder(root.left) 
  
        # Finally recur on right child 
        printPreorder(root.right)
        
print("Preorder traversal of binary tree is:")
printPreorder(root) 
  
print("\nInorder traversal of binary tree is:")
printInorder(root)