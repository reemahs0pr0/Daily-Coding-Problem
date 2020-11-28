# A unival tree (which stands for "universal value") is a tree where 
# all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
root = Node(1, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))

def is_univ(node):
    if node.left == node.right == None:
        return True
    elif node.left == None and node.right != None:
        if is_univ(node.right) and node.val == node.right.val:
            return True
        else:
            return False
    elif node.left != None and node.right == None:
        if is_univ(node.left) and node.val == node.left.val:
            return True
        else:
            return False
    else:
        if node.val == node.left.val == node.right.val and \
        is_univ(node.right) and is_univ(node.left):
            return True
        else:
            return False
        
def num_of_univ(root, count=0):
    if is_univ(root):
        count += 1
    if root.left != None:
        count = num_of_univ(root.left, count)
    if root.right != None:
        count = num_of_univ(root.right, count)
    return count

print(num_of_univ(root))