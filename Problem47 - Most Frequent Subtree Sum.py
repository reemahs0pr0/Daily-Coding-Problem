# Given the root of a binary tree, find the most frequent subtree sum. The subtree sum of a node is the sum of all values under a node, including the node itself.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def add_subtree_sum(graph, tree):
    r = tree.right.val if tree.right is not None else 0
    l = tree.left.val if tree.left is not None else 0
    sum = tree.val + r + l
    if (sum not in graph):
        graph[sum] = 1
    else:
        graph[sum] = graph[sum] + 1
    if (tree.left is not None):
        add_subtree_sum(graph, tree.left)
    if (tree.right is not None):
        add_subtree_sum(graph, tree.right)
    return

def most_frequent_subtree_sum(graph):
    greatest_key = None
    greatest_value = 1
    for key in graph:
        if (graph[key] > greatest_value):
            greatest_key = key
    return greatest_key

tree = Node(56, Node(23, Node(-69, Node(10), Node(5)), Node(55, Node(9), Node(62))), Node(-36, Node(72, Node(88), Node(97)), Node(-22, Node(17), Node(81))))
graph = {}
add_subtree_sum(graph, tree)
print(graph)
print('Most frequent subtree sum: ' + str(most_frequent_subtree_sum(graph)))