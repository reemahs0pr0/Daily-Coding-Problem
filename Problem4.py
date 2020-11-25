# Given the root to a binary tree, implement serialize(root), which 
# serializes the tree into a string, and deserialize(s), which 
# deserializes the string back into the tree.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def insert_right(self, val):
        if self.right is None:
            self.right = Node(val)
        else:
            self.right.insert_right(val)
    
    def insert_left(self, val):
        if self.left is None:
            self.left = Node(val)
        else:
            self.left.insert_left(val)

def serialize(node):
    if 'serial' not in locals():
        serial = ''
    if node.left:
        serial += serialize(node.left)
    serial += node.val + ' '
    if node.right:
        serial += serialize(node.right)
    return serial

def deserialize(serial):
    arr = serial.split()
    index = 0
    for i in range(len(arr)):
        if arr[i] == 'root':
            index = i
            break
    root = Node(arr[i])
    for i in range(index+1, len(arr)):
        root.insert_right(arr[i])
    for i in range(index-1, -1, -1):
        root.insert_left(arr[i])
    return root

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'