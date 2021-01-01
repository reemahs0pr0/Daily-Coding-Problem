# The power set of a set is the set of all its subsets. Write a function 
# that, given a set, generates its power set.
# For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, 
#  {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
# You may also use a list or array to represent a set.

s = {1, 2, 3, 4, 5}
l = list(s)
d = {}

for i in range(len(l)+1):
    if i == 0:
        d[1] = []
    else:
        key = 1
        for j in range(pow(2, i-1)+1, pow(2, i)+1):
            val = d[key]
            d[j] = val + l[i-1:i]
            key += 1

power_sets = [{}]
for subset in d.values():
    power_sets.append(set(subset))
power_sets.pop(1)
    
print(power_sets)