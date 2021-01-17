# Implement a queue using two stacks. Recall that a queue is a FIFO 
# (first-in, first-out) data structure with the following methods: enqueue, 
# which inserts an element into the queue, and dequeue, which removes it.

class Stack:
    
    def __init__(self, arr=None):
        if arr==None:
            self.arr = []
        else:
            self.arr = arr
    
    def add(self, elem):
        self.arr.append(elem)
        
    def remove(self):
        return self.arr.pop()
        
    def show(self):
        print(self.arr)
        
class Queue:
    
    def __init__(self, arr=None):
        self.arr = Stack(arr)
    
    def enqueue(self, elem):
        self.arr.add(elem)
        
    def dequeue(self):
        stack = Stack()
        length_1 = len(self.arr.arr)
        for i in range(length_1):
            stack.add(self.arr.remove())
        stack.remove()
        length_2 = len(stack.arr)
        for i in range(length_2):
            self.arr.add(stack.remove())
            
    def show(self):
        self.arr.show()
        
queue = Queue()
for i in range(10):
    queue.enqueue(i)
queue.show()
for i in range(5):
    queue.dequeue()
queue.show()
for i in range(10):
    queue.enqueue(i)
queue.show()
for i in range(6):
    queue.dequeue()
queue.show()