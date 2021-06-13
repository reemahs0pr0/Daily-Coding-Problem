# Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome, as well as 888. 678 is not a palindrome. Do not convert the integer into a string.

def is_palindrome(integers):
    length = len(integers)
    result = True
    for i in range(length//2):
        if (integers[i] != integers[length-1-i]):
            result = False
    return result

def check_palindrome(integer):
    integers = []
    while (integer != 0):
        integers.append(integer%10)
        integer = integer//10
    return is_palindrome(integers)

integer = 6781241251
print(check_palindrome(integer))