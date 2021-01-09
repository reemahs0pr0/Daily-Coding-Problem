# Given an array of numbers, find the maximum sum of any contiguous subarray 
# of the array.
# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum 
# would be 137, since we would take elements 42, 14, -5, and 86.
# Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would 
# not take any elements.
# Do this in O(N) time.

import random

# uncomment to print out the contiguous subarray
def max_sum_of_contiguous_arr(arr):
    maximum = 0
    max_arr = []
    # end_index = 0
    # start_index = 0
    for i in range(len(arr)):
        maximum = max(arr[i], maximum + arr[i])
        max_arr.append(maximum)
    maximum = max(max_arr)
    # for i in range(len(max_arr)-1, -1, -1):
    #     if max_arr[i] == maximum:
    #         end_index = i
    #     if max_arr[i] == arr[i] and i <= end_index:
    #         start_index = i
    #         break
    if maximum < 0:
        # print([])
        print(0)
    else:
        # print(arr[start_index:end_index+1])
        print(maximum)
        
arr = []
for i in range(10):
    arr.append(random.randint(-99,99))
print(arr)
max_sum_of_contiguous_arr(arr)