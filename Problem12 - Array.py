# You run an e-commerce website and want to record the last N order ids 
# in a log. Implement a data structure to accomplish this, with the 
# following API:
# •	record(order_id): adds the order_id to the log
# •	get_last(i): gets the ith last element from the log. i is 
# guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible.

class Log:
    def __init__(self):
        self.log = []
    def record(self, order_id):
        self.log.append(order_id)
    def get_last(self, i):
        print(self.log[len(self.log)-i:])
    
x = Log()
x.record(1)
x.record(2)
x.record(3)
x.record(4)
x.record(5)
x.record(6)
x.get_last(3)