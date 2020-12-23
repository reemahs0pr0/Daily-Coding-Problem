# Compute the running median of a sequence of numbers. That is, given a 
# stream of numbers, print out the median of the list so far on each new 
# element.
# Recall that the median of an even-numbered list is the average of the 
# two middle numbers.

arr = [2, 1, 5, 7, 2, 0, 5]

for i in range(1, len(arr)+1):
    new_arr = arr[:i]
    new_arr.sort()
    if i == 1:
        print(new_arr[0])
    elif i%2 == 0:
        median = (new_arr[int(i/2)] + new_arr[int(i/2)-1])/2
        print(int(median) if median%2 == 0 else median)
    else:
        print(new_arr[int((i-1)/2)])