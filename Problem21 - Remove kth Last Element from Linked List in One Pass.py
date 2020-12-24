# Given a singly linked list and an integer k, remove the kth last element 
# from the list. k is guaranteed to be smaller than the length of the list.
# The list is very long, so making more than one pass is prohibitively 
# expensive.
# Do this in constant space and in one pass.

class Node:
    def __init__(self, val, nex=None):
        self.val = val
        self.nex = nex
    
    def add(self, val):
        if self.nex is None:
            self.nex = Node(val)
        else:
            self.nex.add(val)
            
    def remove(self, index):
        if self.get(index).nex is None:
            self.get(index-1).nex = None
        else:
            self.get(index-1).nex = self.get(index+1)
        
    def get(self, index, i=0):
        if i == index:
            return self
        else:
            i += 1
            return self.nex.get(index, i=i)
    
    def got_next(self):
        if self.nex != None:
            return True
        return False
    
linkedList = Node(1)
for i in range(2, 101):
    linkedList.add(i)

k = 32
i = k
while i >= k:
    if linkedList.get(i).got_next():
        i += 1
    else:
        linkedList.remove(i-k+1)
        break
    
j = 0
while j >= 0:
    print(linkedList.get(j).val)
    if linkedList.get(j).got_next():
        j += 1
    else:
        break