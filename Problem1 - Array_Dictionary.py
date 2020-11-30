# Given a list of numbers and a number k, return whether any two numbers 
# from the list add up to k. For example, given [10, 15, 3, 7] and k of 
# 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

arr = [10, 15, 3, 8, 2, 7] 
k = 17
dict = {}

def check_addup(arr, k):
    for num in arr:
        if num not in dict:
            dict[num] = 1
            dict[k-num] = 0
        elif dict[num] == 0:
            return "%s and %s added up to %s" % (k-num, num, k)
    return "No numbers added up to %s" % k

print(check_addup(arr, k))