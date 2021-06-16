# Given an integer, find the next permutation of it in absolute order. For example, given 48975, the next permutation would be 49578.

def find_next_permutation(integer):
    string_integer = str(integer)
    result = []
    digits_after = []
    next_digit = None
    for i in range(len(string_integer)-2, -1, -1):
        digits_after.append(string_integer[i+1])
        for j in range(len(digits_after)):
            if (int(digits_after[j]) > int(string_integer[i])):
                if (next_digit == None):
                    next_digit = digits_after[j]
                elif (int(digits_after[j]) < int(next_digit)):
                    next_digit = digits_after[j]
        if (next_digit != None):
            for k in range(i):
                result.append(string_integer[k])
            result.append(next_digit)
            digits_after.remove(next_digit)
            digits_after.append(string_integer[i])
            digits_after.sort()
            for k in range(len(digits_after)):
                result.append(digits_after[k]) 
            break    
    if (next_digit == None):
        print("No next permutation found.")
    else:       
        print("Next permutation: " + ''.join(result))

integer = int(input("Input an integer: "))
find_next_permutation(integer)