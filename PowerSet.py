def powerset(l):
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
    return power_sets

if __name__ == '__main__':
    s = {1, 2, 3, 4, 5}
    print(powerset(list(s)))