# Given the root to a binary search tree, find the second largest node 
# in the tree.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
tree = Node(56, Node(23, Node(69, Node(10), Node(5)), Node(55, Node(9), Node(62))), \
            Node(36, Node(72, Node(88), Node(97)), Node(22, Node(17), Node(81))))
sec_largest = 0

def my_function(root, largest):
    global sec_largest
    maximum = max(root.left.val if root.left != None else 0, \
                  root.right.val if root.right != None else 0 )
    minimum = min(root.left.val if root.left != None else 0, \
              root.right.val if root.right != None else 0 )
    if maximum > largest and minimum > largest:
        sec_largest = minimum
        largest = maximum
    elif maximum > largest and minimum < largest:
        sec_largest = largest
        largest = maximum
    elif maximum < largest and maximum > sec_largest:
        sec_largest = maximum
        
    if root.left == root.right == None:
        return largest
    elif root.left == None and root.right != None:
        largest = my_function(root.right, largest)
    elif root.left != None and root.right == None:
        largest = my_function(root.left, largest)
    else:
        largest = my_function(root.right, largest)
        largest = my_function(root.left, largest)
    return largest
    
my_function(tree, tree.val)
print(sec_largest)