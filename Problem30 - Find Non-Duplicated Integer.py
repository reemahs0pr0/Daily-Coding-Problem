# Given an array of integers where every integer occurs three times 
# except for one integer, which only occurs once, find and return the 
# non-duplicated integer.
# For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given 
# [13, 19, 13, 13], return 19.
# Do this in O(N) time and O(1) space.

from Quicksort import quicksort

arr1 = [6, 1, 3, 3, 3, 6, 6]
arr2 = [13, 19, 13, 13]
arr3 = [23, 13, 19, 13, 10, 13, 19, 19, 5, 10, 5, 23, 5, 24, 23, 10]
quicksort(arr1, 0, len(arr1)-1)
quicksort(arr2, 0, len(arr2)-1)
quicksort(arr3, 0, len(arr3)-1)

def non_duplicate(arr):
    i = 0
    while True:
        if i == len(arr)-1:
            return arr[i]
        elif arr[i] == arr[i+1]:
            i += 3
        else:
            return arr[i]
        
print(non_duplicate(arr1))
print(non_duplicate(arr2))
print(non_duplicate(arr3))