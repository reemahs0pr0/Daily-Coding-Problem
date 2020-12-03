# There exists a staircase with N steps, and you can climb up either 1 or 
# 2 steps at a time. Given N, write a function that returns the number of 
# unique ways you can climb the staircase. The order of the steps matters.
# For example, if N is 4, then there are 5 unique ways:
# •	1, 1, 1, 1
# •	2, 1, 1
# •	1, 2, 1
# •	1, 1, 2
# •	2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you 
# could climb any number from a set of positive integers X? For example, 
# if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

def num_ways_recursion(N, X):
    if N == 0:
        return 1
    else:
        result = 0
        for i in range(len(X)):
            if N >= X[i]:
                result += num_ways_recursion(N-X[i], X)
            else:
                break
        return result

def num_ways_memoized(N, memo, X):
    if N == 0:
        return 1
    else:
        if memo[N] != None:
            return memo[N]
        else:
            memo[N] = 0
            for i in range(len(X)):
                if N >= X[i]:
                    memo[N] += num_ways_memoized(N-X[i], memo, X)
                else:
                    break
            return memo[N]

import time

N = 40
X = {1, 3, 5}
X = list(X)

time1 = time.time()
print(num_ways_recursion(N, X))
print("Time for basic recursion approach: %s" % (time.time()-time1) + "\n")

memo = [None] * (N+1)
time1 = time.time()
print(num_ways_memoized(N, memo, X))
print("Time for memoized approach: %s" % (time.time()-time1) + "\n")