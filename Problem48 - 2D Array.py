# Let A be an N by M matrix in which every row and every column is sorted.
# Given i1, j1, i2, and j2, compute the number of elements of M smaller than M[i1, j1] and larger than M[i2, j2].

def special_function(matrix, i1, j1, i2, j2):
    s = matrix[i1][j1]
    l = matrix[i2][j2]
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if ((i <= i1 and matrix[i][j] < s) or (i > i1 and j < j1 and matrix[i][j] < s) or (i <= i2 and j > j2 and matrix[i][j] > l) or (i > i2 and matrix[i][j] > l)):
                count += 1
    print(count)


M = [[1, 3, 7, 10, 15, 20],
    [2, 6, 9, 14, 22, 25],
    [3, 8, 10, 15, 25, 30],
    [10, 11, 12, 23, 30, 35],
    [20, 25, 30, 35, 40, 45]]

special_function(M, 1, 1, 3, 3)