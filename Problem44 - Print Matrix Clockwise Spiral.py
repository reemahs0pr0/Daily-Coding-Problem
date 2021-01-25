# Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

matrix = [[1,  2,  3,  4,  5],
          [6,  7,  8,  9,  10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25],
          [26, 27, 28, 29, 30]]

def print_matrix_clockwise_spiral(matrix):
    i = 0
    while len(matrix) != 0:
        if i == 0:
            for j in range(len(matrix[i])):
                print(matrix[i][j])
            matrix.pop(i)
            if len(matrix) == 0:
                break
            print(matrix[i][len(matrix[i])-1])
            matrix[i].pop(len(matrix[i])-1)
            i += 1
        elif i == len(matrix) - 1 or len(matrix) == 1:
            if len(matrix) == 1:
                i = 0
            for j in range(len(matrix[i])-1, -1, -1):
                print(matrix[i][j])
            matrix.pop(i)
            for k in range(len(matrix)-1, 0, -1):
                print(matrix[k][0])
                matrix[k].pop(0)
            i = 0
        else:
            print(matrix[i][len(matrix[i])-1])
            matrix[i].pop(len(matrix[i])-1)
            i += 1
            
print_matrix_clockwise_spiral(matrix)