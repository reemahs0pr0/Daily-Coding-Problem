# Run-length encoding is a fast and simple method of encoding strings. The 
# basic idea is to represent repeated successive characters as a single count 
# and character. For example, the string "AAAABBBCCDAA" would be encoded as 
# "4A3B2C1D2A".
# Implement run-length encoding and decoding. You can assume the string to be 
# encoded have no digits and consists solely of alphabetic characters. You can 
# assume the string to be decoded is valid.

string = "JJJJJJJJDDDDDDDPPPPPWWWWWWWWWKKKKKKKKKKKKSSSSSSSMMMMMMFFFFFFMMMMMWP"

def encode(string):
    char_check = string[:1]
    count = 1
    encoded_string = ""
    
    for c in string[1:]:
        if c == char_check:
            count += 1
        else:
            encoded_string += str(count) + char_check
            count = 1
            char_check = c
    encoded_string += str(count) + char_check
    return encoded_string

print(encode(string))