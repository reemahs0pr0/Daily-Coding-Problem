# Given two singly linked lists that intersect at some point, find the 
# intersecting node. The lists are non-cyclical.
# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, 
# return the node with value 8.
# In this example, assume nodes with the same value are the exact same 
# node objects.
# Do this in O(M + N) time (where M and N are the lengths of the lists) 
# and constant space.

class Node:
    def __init__(self, val, prev=None, nex=None):
        self.val = val
        self.prev = prev
        self.nex = nex
    
    def add(self, val):
        if self.nex is None:
            self.nex = Node(val, self)
        else:
            self.nex.add(val)
            
    def get(self, index, i=0):
        if i == index:
            return self
        else:
            i += 1
            return self.nex.get(index, i=i)
        
    def insert(self, val, index):
        self.get(index).prev = Node(val, self.get(index-1), 
                                          self.get(index))
        self.get(index-1).nex = Node(val, self.get(index-1), 
                                           self.get(index))
        
    def getLength(self, count=1):
        if self.nex:
            count += 1
            return self.nex.getLength(count=count)
        return count
    
    def remove(self, index):
        self.get(index-1).nex = self.get(index+1)
        self.get(index).prev = self.get(index-1)
        
A = Node(3)
A.add(8)
A.add(1)
A.add(10)

B = Node(99)
B.add(1)
B.add(8)
B.add(7)

for i in range(A.getLength()):
    print(A.get(i).val, end=" -> " if i != B.getLength()-1 else " ")

print()

for i in range(B.getLength()):
    print(B.get(i).val, end=" -> " if i != B.getLength()-1 else " ")
    
dictionary = {}
intersecting_node = None
    
for i in range(min(A.getLength(), B.getLength())):
    if A.get(i).val not in dictionary:
        dictionary[A.get(i).val] = "A"
    if A.get(i).val in dictionary:
        if dictionary[A.get(i).val] == "B":
            intersecting_node = A.get(i)
            break
    if B.get(i).val not in dictionary:
        dictionary[B.get(i).val] = "B"
    if B.get(i).val in dictionary:
        if dictionary[B.get(i).val] == "A":
            intersecting_node = B.get(i)
            break

if intersecting_node == None:
    print("\nNo intersecting node.")
else:
    print("\nIntersecting node is " + str(intersecting_node.val))