# Given a set of distinct positive integers, find the largest subset such that every pair of elements in the subset (i, j) satisfies either i % j = 0 or j % i = 0.
# For example, given the set [3, 5, 10, 20, 21], you should return [5, 10, 20]. Given [1, 3, 6, 24], return [1, 3, 6, 24].

def largest_set(l):
    final_l = []
    for i in range(len(l)):
        if (l[i] in set(final_l)):
            continue
        else:
            temp_l = []
            temp_l.append(l[i])
        for j in range(i+1, len(l)):
            length = len(temp_l)
            for k in range(length):
                if (l[j] % temp_l[k] != 0):
                    break
                if (l[j] % temp_l[k] == 0 and k == length-1):
                    temp_l.append(l[j])
        if (len(temp_l) >= len(final_l)):
            final_l = temp_l
            temp_l = []
    print(final_l)
    
l = [1, 3, 5, 6, 9, 10, 15, 20, 30, 40, 50]
largest_set(l)