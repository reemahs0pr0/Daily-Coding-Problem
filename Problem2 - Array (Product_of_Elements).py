# Given an array of integers, return a new array such that each element at 
# index i of the new array is the product of all the numbers in the 
# original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would 
# be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected 
# output would be [2, 3, 6].
# Follow-up: what if you can't use division?

arr = [1, 2, 3, 4, 5]
product = 1
new_arr = []
for num in arr:
    product *= num
for num in arr:
    new_arr.append(int(product/num))
print(new_arr)

newer_arr = []
for num in arr:
    newer_arr.append(1)
for i in range(len(newer_arr)):
    for j in range(len(arr)):
        if i == j:
            continue
        newer_arr[i] *= arr[j]
print(newer_arr)