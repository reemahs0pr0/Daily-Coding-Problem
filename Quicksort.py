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
        if arr[j] < pivot:
            i += 1
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
    temp = arr[r]
    arr[r] = arr[i+1]
    arr[i+1] = temp
    return i+1