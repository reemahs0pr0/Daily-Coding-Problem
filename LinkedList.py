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
        self.get(index).prev = Node(val, self.get(index-1), self.get(index))
        self.get(index-1).nex = self.get(index).prev
        
    def getLength(self, count=1):
        if self.nex:
            count += 1
            return self.nex.getLength(count=count)
        return count
    
    def remove(self, index):
        self.get(index-1).nex = self.get(index+1)
        self.get(index).prev = self.get(index-1)
    
def print_linked_list(linkedList):
    for i in range(linkedList.getLength()):
        print(linkedList.get(i).val, end=", " if i != linkedList.getLength()-1 else "")
    print()

def print_linked_list_backwards(node, arr=[]):
    arr.append(node.val)
    if node.nex:
        print_linked_list_backwards(node.nex, arr)
    else:
        for i in range(len(arr)-1, -1, -1):
            print(arr[i], end=", " if i != 0 else "")    

if __name__ == '__main__':
    linkedList = Node(1)
    linkedList.add(2)
    linkedList.add(3)
    linkedList.add(92)
    linkedList.add(54)
    linkedList.add(9)
    linkedList.add(10)
    print_linked_list(linkedList)
    linkedList.insert(99, 5)
    print_linked_list(linkedList)
    linkedList.insert(69, 3)
    print_linked_list(linkedList)
    linkedList.remove(3)
    print_linked_list(linkedList)
    linkedList.remove(5)
    print_linked_list(linkedList)
    print("Length: " + str(linkedList.getLength()))

    print_linked_list_backwards(linkedList)
