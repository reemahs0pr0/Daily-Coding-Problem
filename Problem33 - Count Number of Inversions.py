# We can determine how "out of order" an array A is by counting the number 
# of inversions it has. Two elements A[i] and A[j] form an inversion if 
# A[i] > A[j] but i < j. That is, a smaller element appears after a larger 
# element.
# Given an array, count the number of inversions it has. Do this faster 
# than O(N^2) time.
# You may assume each element in the array is distinct.
# For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5]
# has three inversions: (2, 1), (4, 1), and (4, 3). The array 
# [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an 
# inversion.

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)

def merge(left, right):
    global count
    arr = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            arr.append(left[0])
            left.remove(left[0])
        else:
            count += len(left) #add one more line to count no. of inversions
            arr.append(right[0])
            right.remove(right[0])
        
    if len(left) == 0:
        arr = arr + right
    else:
        arr = arr + left
    return arr

count = 0
arr = [5, 4, 3, 2, 1]
mergesort(arr)
print(count)