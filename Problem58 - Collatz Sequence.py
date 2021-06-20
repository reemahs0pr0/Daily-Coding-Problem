# A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:
# •	if n is even, the next number in the sequence is n / 2
# •	if n is odd, the next number in the sequence is 3n + 1 
# It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.
# Bonus: What input n <= 1000000 gives the longest sequence?

def collatz_seq(num):
    # print(num, end=" ")
    count = 1
    while num > 1:
        if num%2 == 0:
            num = int(num/2)
            count += 1
            # print(num, end=" ")
        else:
            num = int(3*num+1)
            count += 1
            # print(num, end=" ")
    return count
    
max = 0
input = None
for i in range(1, 1000000+1):
    if collatz_seq(i) > max:
        max = collatz_seq(i)
        input = i
print(input)