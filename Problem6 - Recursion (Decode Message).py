# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, 
# count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded 
# as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is 
# not allowed.

def num_of_ways(message):
    if len(message) in range(2):
        return 1
    if message[0] == '0':
        return 0
    result = num_of_ways(message[1:])
    if int(message[0:2]) <= 26:
        result += num_of_ways(message[2:])
    return result

print(num_of_ways('111'))