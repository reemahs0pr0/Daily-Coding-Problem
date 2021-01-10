# Suppose an arithmetic expression is given as a binary tree. Each leaf is an 
# integer and each internal node is one of '+', '−', '∗', or '/'.
# Given the root to such a tree, write a function to evaluate it.
# For example, given the following tree:
#     *
#    / \
#   +    +
#  / \  / \
# 3  2  4  5
# You should return 45, as it is (3 + 2) * (4 + 5).

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def evaluate_tree(node):
    global new_root
    if node.left != None and isinstance(node.left.val, (float, int)) and \
    node.right != None and isinstance(node.right.val, (float, int)):
        if node.val == '+':
            node.val = node.left.val + node.right.val
        elif node.val == '-':
            node.val = node.left.val - node.right.val
        elif node.val == '*':
            node.val = node.left.val * node.right.val
        elif node.val == '/':
            node.val = node.left.val / node.right.val
        new_root = node.val
        return
    if node.left != None and not isinstance(node.left.val, (float, int)):
        evaluate_tree(node.left)
    if node.right != None and not isinstance(node.right.val, (float, int)):
        evaluate_tree(node.right)
        
node = Node('+', Node('+', Node(2), Node('*', Node(3), Node(4))), \
            Node('/', Node('*', Node(3), Node(4)), Node(5)))
new_root = None

while node.val != new_root:
    evaluate_tree(node)
print(new_root)