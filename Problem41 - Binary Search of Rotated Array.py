# An sorted array of integers was rotated an unknown number of times.
# Given such an array, find the index of the element in the array in faster 
# than linear time. If the element doesn't exist in the array, return null.
# For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, 
# return 4 (the index of 8 in the array).
# You can assume all the integers in the array are unique.

arr = [13, 18, 25, 2, 8, 10]
target = 8
left = 0
right = len(arr) - 1
result = None
while (left <= right):
    middle = int((left + right) / 2)
    # print(arr[middle])
    # print(arr[left:right+1])
    if (arr[middle] == target):
        result = middle
        break
    elif (arr[middle] < arr[len(arr)-1]):
        if (arr[middle] < target and target <= arr[len(arr)-1]):
            left = middle + 1
        else:
            right = middle - 1
    elif (arr[middle] > arr[0]):
        if (arr[middle] > target and target >= arr[0]):
            right = middle - 1
        else:
            left = middle + 1
print(result)