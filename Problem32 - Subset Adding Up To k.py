# Given a list of integers S and a target number k, write a function that 
# returns a subset of S that adds up to k. If such a subset cannot be made, 
# then return null.
# Integers can appear more than once in the list. You may assume all numbers 
# in the list are positive.
# For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] 
# since it sums up to 24.

from PowerSet import powerset

def subset_added_up_to_k(S, k):
    subsets = powerset(S)
    for subset in subsets:
        subset_list = list(subset)
        sum_result = 0
        for integer in subset_list:
            sum_result += integer
        if sum_result == k:
            return subset_list
        if subset == subsets[len(subsets)-1]:
            return None
    
S = [1,2,3,4,5,6]
k = 15
print(subset_added_up_to_k(S, k))