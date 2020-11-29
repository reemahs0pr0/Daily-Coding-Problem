# A unival tree (which stands for "universal value") is a tree where 
# all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def is_univ(self):
        if self.left == self.right == None:
            return True
        elif self.left == None and self.right != None:
            if self.right.is_univ() and self.val == self.right.val:
                return True
            else:
                return False
        elif self.left != None and self.right == None:
            if self.left.is_univ() and self.val == self.left.val:
                return True
            else:
                return False
        else:
            if self.val == self.left.val == self.right.val and \
            self.right.is_univ() and self.left.is_univ():
                return True
            else:
                return False
        
tree = Node(1, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
        
def num_of_univ(root, count=0):
    if root.is_univ():
        count += 1
    if root.left != None:
        count = num_of_univ(root.left, count)
    if root.right != None:
        count = num_of_univ(root.right, count)
    return count

print(num_of_univ(tree))