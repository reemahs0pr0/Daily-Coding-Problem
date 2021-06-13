# Let user enter two integers. For integers between the two inputs (inclusive), return the number of integers which contain the digit 6 and 8.

input_1 = int(input("Enter first integer: "))
input_2 = int(input("Enter second integer: "))
count = 0
for i in range(input_1, input_2+1):
    if ('6' in str(i) or '8' in str(i)):
        count += 1
print(count)