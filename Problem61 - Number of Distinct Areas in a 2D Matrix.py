def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()

def divide_matrix(matrix):
    queue = []  # to store indices of adjacent elements with same value
    count = 0   # number of area
    char = 65   # to mark checked area
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # if element has not been checked
            if isinstance(matrix[i][j], int):
                # check adjacent element on the right
                if j != len(matrix[i]) - 1:
                    if matrix[i][j] == matrix[i][j+1]:
                        queue.append((i, j+1))
                # check adjacent element below
                if i != len(matrix) -1:
                    if matrix[i][j] == matrix[i+1][j]:
                        queue.append((i+1, j))
                # mark checked element
                matrix[i][j] = chr(char)
                while len(queue) != 0:
                    # current element being checked
                    element = matrix[queue[0][0]][queue[0][1]]
                    # skip and remove from queue if element has been marked
                    if not isinstance(element, int):
                        queue.remove(queue[0])
                        continue
                    # check adjacent element on the right
                    if queue[0][1] != len(matrix[i]) - 1:
                        if element == matrix[queue[0][0]][queue[0][1]+1]:
                            queue.append((queue[0][0], queue[0][1]+1))
                    # check adjacent element below
                    if queue[0][0] != len(matrix) - 1:
                        if element == matrix[queue[0][0]+1][queue[0][1]]:
                            queue.append((queue[0][0]+1, queue[0][1]))
                    # check adjacent element on the left
                    if queue[0][1] != 0:
                        if element == matrix[queue[0][0]][queue[0][1]-1]:
                            queue.append((queue[0][0], queue[0][1]-1))
                    # mark checked element
                    matrix[queue[0][0]][queue[0][1]] = chr(char)
                    # remove index from queue after element with the index has been checked
                    queue.remove(queue[0])
                count += 1
                char += 1
    return count

X = [[2, 2, 8, 6, 2],
     [6, 8, 8, 8, 1],
     [8, 8, 8, 2, 7],
     [3, 3, 3, 3, 7],
     [3, 2, 2, 2, 6],
     [3, 4, 9, 2, 8],
     [3, 4, 4, 4, 4]]

print_matrix(X)
num_of_areas = divide_matrix(X)
print_matrix(X)
print('Total number of areas: ' + str(num_of_areas))