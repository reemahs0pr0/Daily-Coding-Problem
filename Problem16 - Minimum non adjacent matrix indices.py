# A builder is looking to build a row of N house_dict that can be of K 
# different colors. He has a goal of minimizing cost while ensuring 
# that no two neighboring house_dict are of the same color.
# Given an N by K matrix where the nth row and kth column represents 
# the cost to build the nth house with kth color, return the minimum 
# cost which achieves this goal.

import numpy as np

N = 5
K = 5

matrix = np.random.random((N,K)) * 10
print(matrix)
house_dict = {}

for i in range(N):
    house_dict[i+1] = matrix[i][:]

def get_index(house, value):
    for i in range(len(house)):
        if house[i] == value:
            return i

def second_min(house):
    second_min = 99999
    for cost in house:
        if cost == min(house):
            continue
        if cost < second_min:
            second_min = cost
    return second_min

prev_color = 0
color = 0
min_cost = 0
alt_min_cost = 0

for i in range(N):
    prev_color = color
    color = get_index(house_dict[i+1], min(house_dict[i+1]))
    if i==0:
        min_cost += min(house_dict[i+1])
        alt_min_cost += second_min(house_dict[i+1])
    elif color == prev_color:
        minimum = min(min_cost + second_min(house_dict[i+1]), alt_min_cost + 
                       min(house_dict[i+1]))
        maximum = max(min_cost + second_min(house_dict[i+1]), 
                           alt_min_cost + min(house_dict[i+1]))
        min_cost = minimum
        alt_min_cost = maximum
        if minimum == min_cost + second_min(house_dict[i+1]):
            color = get_index(house_dict[i+1], second_min(house_dict[i+1]))
    else:
        min_cost += min(house_dict[i+1])
        if get_index(house_dict[i+1], second_min(house_dict[i+1])) != prev_color:
            alt_min_cost = min_cost + second_min(house_dict[i+1])
        else:
            alt_min_cost = alt_min_cost + second_min(house_dict[i+1])

print()
print(min_cost)