# Given an array of integers, find the first missing positive integer in 
# linear time and constant space. In other words, find the lowest 
# positive integer that does not exist in the array. The array can 
# contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input 
# [1, 2, 0] should give 3.
# You can modify the input array in-place.

arr1 = [3, 4, -1, 1]
arr2 = [1, 2, 0]

from Quicksort import quicksort

quicksort(arr1, 0, len(arr1) - 1)
quicksort(arr2, 0, len(arr2) - 1)

integer1 = 1
for i in range(len(arr1)):
    if arr1[i] == integer1:
        integer1 += 1
print(integer1)

integer2 = 1
for i in range(len(arr2)):
    if arr2[i] == integer2:
        integer2 += 1
print(integer2)