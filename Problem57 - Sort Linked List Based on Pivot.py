# Given a linked list of numbers and a pivot k, partition the linked list so that all nodes less than k come before nodes greater than or equal to k. 
# For example, given the linked list 5 -> 1 -> 8 -> 0 -> 3 and k = 3, the solution could be 1 -> 0 -> 5 -> 8 -> 3.

from LinkedList import print_linked_list
from LinkedList import Node

def sort_from_pivot(linked_list, k):
    small_list = None
    large_list = None
    first_value = linked_list.get(0).val
    if first_value < k:
        small_list = Node(first_value)
    else:
        large_list = Node(first_value)
    for i in range(1, linked_list.getLength()):
        value = linked_list.get(i).val
        if value < k:
            if small_list == None:
                small_list = Node(value)
            else:
                small_list.add(value)
        else:
            if large_list == None:
                large_list = Node(value)
            else:
                large_list.add(value)
    concat(small_list, large_list)
    return small_list

def concat(linkedList1, linkedList2):
    last_node_linkedList1 = linkedList1.get(linkedList1.getLength()-1)
    first_node_linkedList2 = linkedList2.get(0)
    last_node_linkedList1.nex = first_node_linkedList2
    last_node_linkedList1.nex.prev = last_node_linkedList1

linkedList = Node(5)
linkedList.add(1)
linkedList.add(8)
linkedList.add(0)
linkedList.add(3)
linkedList.add(7)
linkedList.add(2)
linkedList.add(9)
print_linked_list(linkedList)

pivot = 7
sorted_linkedList = sort_from_pivot(linkedList, pivot)
print_linked_list(sorted_linkedList)