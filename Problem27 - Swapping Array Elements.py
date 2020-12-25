# Given an array of strictly the characters 'R', 'G', and 'B', segregate 
# the values of the array so that all the Rs come first, the Gs come 
# second, and the Bs come last. You can only swap elements of the array.
# Do this in linear time and in-place.
# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it 
# should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

def quicksort(arr, l, r):
    if l >= r:
        return
    p = partition(arr, l, r)

    quicksort(arr, l, p-1)
    quicksort(arr, p+1, r)

def partition(arr, l, r):
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] =='R' and pivot != 'R' or arr[j] == 'G' and pivot =="B":
            i += 1
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
    temp = arr[r]
    arr[r] = arr[i+1]
    arr[i+1] = temp
    return i+1

arr = ['G', 'B', 'R', 'R', 'B', 'R', 'G', 'B', 'G', 'G', 'B', 'G', 'R', 'B']
quicksort(arr, 0, len(arr)-1)
print(arr)