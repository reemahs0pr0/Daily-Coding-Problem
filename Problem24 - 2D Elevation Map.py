# You are given an array of non-negative integers that represents a 
# two-dimensional elevation map where each element is unit-width wall and the 
# integer is the height. Suppose it will rain and all spots between two walls 
# get filled up.
# For example, given the input [2, 1, 2], we can hold 1 unit of water in the 
# middle.
# Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index,
# 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would 
# run off to the left), so we can trap 8 units of water.

import numpy as np

walls = [9, 10, 7, 0, 1, 4, 2, 2, 10]
unit = 0
start = False
prev_walls = walls.copy()
print(walls)

def fillup(arr, start, end):
    minimum = min(arr[start], arr[end])
    unit = 0
    for i in range(start+1, end):
        if minimum > arr[i]:
            unit += minimum - arr[i]
            arr[i] = minimum
    return unit

for j in range(int(len(walls)/2)):
    for i in range(len(walls)):
        if i == 0:
            left = i
        elif walls[i] >= walls[i-1] and start == False:
            left = i
        elif walls[i] > walls[i-1] and start == True:
            right = i
            unit += fillup(walls, left, right)
            left = i 
            start = False
        else:
            start = True
    if np.array_equal(walls, prev_walls):
        break
    else:
        prev_walls = walls.copy()
    print(walls)
    
print(unit)        