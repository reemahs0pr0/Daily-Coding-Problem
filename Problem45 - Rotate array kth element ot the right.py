# Given an array and a number k that's smaller than the length of the array, rotate the array to the right k elements in-place.

arr = [4, 86, 1, 8, 45, 1, 67, 10, 3, 35]
k = 5

def rotate_array(arr, k):
    for i in range(k):
        replacing = arr[len(arr)-1]
        for j in range(len(arr)):
            replaced = arr[j]
            arr[j] = replacing
            replacing = replaced 
    print(arr)

rotate_array(arr, k)