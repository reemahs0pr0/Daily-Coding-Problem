# Given a list of integers, write a function that returns the largest 
# sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, 
# and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

arr1 = [2, 4, 6, 2, 5]
arr2 = [5, 1, 1, 5]

def largest_sum_of_non_adjacent_elements(arr):
    for i in range(len(arr)):
        if i == 0:
            incl = arr[i]
            excl = 0
        else:
            temp = incl
            incl = max(temp, excl + arr[i])
            excl = temp
        if i == len(arr) -1:
            print(incl)
            
largest_sum_of_non_adjacent_elements(arr1)
largest_sum_of_non_adjacent_elements(arr2)