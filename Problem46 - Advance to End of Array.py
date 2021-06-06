# You are given an array of nonnegative integers. Let's say you start at the beginning of the array and are trying to advance to the end. You can advance at most, the number of steps that you're currently on. Determine whether you can get to the end of the array.
# For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices 0 -> 1 -> 3 -> 5, so return true.
# Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.

def reach_end(arr, index=0):
    if (index >= len(arr)):
        return True
    result = False
    for i in range(arr[index]):
        result = reach_end(arr, index+i+1)
        if (result == True):
            break
    return result

arr = [1, 3, 1, 0, 2, 0]
print(reach_end(arr))