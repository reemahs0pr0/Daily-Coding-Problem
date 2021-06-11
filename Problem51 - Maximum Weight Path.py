# You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers. For example, [[1], [2, 3], [1, 5, 1], [4, 6, 7, 8]] represents the triangle:
#    1
#   2 3
#  1 5 1
# 4 6 7 8
# We define a path in the triangle to start at the top and go down one row at a time to an adjacent value, eventually ending with an entry on the bottom row. For example, 1 -> 3 -> 5 -> 7. The weight of the path is the sum of the entries.
# Write a program that returns the weight of the maximum weight path.

def maximum_weigth_path(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr[i])):
            if (j == 0):
                arr[i][j] += arr[i-1][j]
            elif (j == len(arr[i])-1):
                arr[i][j] += arr[i-1][j-1]
            else:
                arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])
    print(max(arr[i]))

arr = [[1], [2, 3], [1, 5, 1], [4, 6, 7, 8]]
maximum_weigth_path(arr)