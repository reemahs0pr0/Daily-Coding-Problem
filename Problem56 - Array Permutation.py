# A permutation can be specified by an array P, where P[i] represents the location of the element at i in the permutation. For example, [2, 1, 0] represents the permutation where elements at the index 0 and 2 are swapped.
# Given an array and a permutation, apply the permutation to the array. For example, given the array ["a", "b", "c"] and the permutation [2, 1, 0], return ["c", "b", "a"].

def permute_array(arr, permutation):
    result = []
    dict = {}
    for i in range(len(arr)):
        dict[i] = arr[i]
    for i in range(len(permutation)):
        result.append(dict[permutation[i]])
    return result

P = ["a", "b", "c"]
permutation = [2, 1, 0]
permuted_P = permute_array(P, permutation)
print(permuted_P)