# Suppose you are given two lists of n points, one list p1, p2, ..., pn on the line y = 0 and the other list q1, q2, ..., qn on the line y = 1. Imagine a set of n line segments connecting each point pi to qi. Write an algorithm to determine how many pairs of the line segments intersect.

def gradient_list(p, q):
    arr = []
    for i in range(len(p)):
        arr.append(p[i] - q[i])
    return arr

def number_of_intersection(gradient):
    count = 0
    for i in range(len(gradient)):
        for j in range(i+1, len(gradient)):
            if (gradient[i] != gradient[j]):
                count += 1
    print(count)

p = [-7, -2, 2, 5, 8]
q = [-7, -2, 2, 5, 9]

gradient = gradient_list(p, q)
number_of_intersection(gradient)