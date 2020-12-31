# Given an array of integers where every integer occurs three times 
# except for one integer, which only occurs once, find and return the 
# non-duplicated integer.
# For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given 
# [13, 19, 13, 13], return 19.
# Do this in O(N) time and O(1) space.

from Quicksort import quicksort
import random

def generate(size):
    low = 1
    high = 99
    arr = []
    used = set()
    num = random.randint(low, high)
    for k in range(3):
        arr.append(num)
    length = len(arr)
    used.add(num)
    for i in range(3, size-1, 3):
        num = random.randint(low, high)
        while num in used:
            num = random.randint(low, high)
        used.add(num)
        for j in range(3):
            index = random.randint(0,length-1)
            arr.insert(index, num)
            length += 1
    num = random.randint(low, high)
    while num in used:
        num = random.randint(low, high)
    index = random.randint(0,length-1)
    arr.insert(index, num)
    return arr

def non_duplicate(arr):
    i = 0
    while True:
        if i == len(arr)-1:
            return arr[i]
        elif arr[i] == arr[i+1]:
            i += 3
        else:
            return arr[i]
    
# arg of generate() is length of arr where length = 3x + 1 and x is the
# number of repeated integers
test = generate(7)
print(test)
quicksort(test, 0, len(test)-1)
print(non_duplicate(test))