# Implement an autocomplete system. That is, given a query string s and 
# a set of all possible query strings, return all strings in the set 
# that have s as a prefix.
# For example, given the query string de and the set of strings 
# [dog, deer, deal], return [deer, deal].
# Hint: Try preprocessing the dictionary into a more efficient data 
# structure to speed up queries.

query = "de"
arr = ["dog", "deer", "deal"]

class Node:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node("")
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = Node(char)
                node.children[char] = new_node
                node = new_node 
        node.is_end = True
        
    def traverse(self, node, prefix):
        if node.is_end:
            self.output.append((prefix + node.char))
        else:
            for child in node.children.values():
                self.traverse(child, prefix + node.char)
        
    def query(self, x):
        self.output = []
        node = self.root
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        self.traverse(node, x[:-1])
        print(self.output)
    
t = Trie()
for string in arr:
    t.insert(string)
t.query(query)