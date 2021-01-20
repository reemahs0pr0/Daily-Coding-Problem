# Given a multiset of integers, return whether it can be partitioned into two 
# subsets whose sums are the same.
# For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return 
# true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which 
# both add up to 55.
# Given the multiset {15, 5, 20, 10, 35}, it would return false, since we 
# can't split it up into two subsets that add up to the same sum.

l = [15, 5, 20, 10, 35, 15, 10]
d = {}

for i in range(len(l)+1):
    if i == 0:
        d[1] = []
    else:
        key = 1
        for j in range(pow(2, i-1)+1, pow(2, i)+1):
            if j > pow(2, len(l)-1):
                break
            val = d[key]
            d[j] = val + l[i-1:i]
            key += 1

def check_sum(list_1, list_2):
    if sum(list_1) == sum(list_2):
        return True
    return False

for subset in d.values():
    if check_sum(subset, [x for x in l if x not in subset]):
        print(str(subset) + '\t' + str([x for x in l if x not in subset]))