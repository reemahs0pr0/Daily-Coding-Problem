# There is an N by M matrix of zeroes. Given N and M, write a function to 
# count the number of ways of starting at the top-left corner and getting to 
# the bottom-right corner. You can only move right or down.
# For example, given a 2 by 2 matrix, you should return 2, since there are two 
# ways to get to the bottom-right:
# •	Right, then down
# •	Down, then right
# Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

def generate_matrix(size):
    matrix = []
    for i in range(size[0]):
        matrix.append([0] * size[1])
    return matrix

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
        
def get_num_of_ways(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == 0 or j == 0:
                matrix[i][j] = 1
            else:
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
    print('Total number of ways = ' + \
          str(matrix[len(matrix)-1][len(matrix[len(matrix)-1])-1]), end='\n\n')
    
matrix_size = (5, 10)
matrix = generate_matrix(matrix_size)
get_num_of_ways(matrix)
print_matrix(matrix)