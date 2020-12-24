# The edit distance between two strings refers to the minimum number of 
# character insertions, deletions, and substitutions required to change one 
# string to the other. For example, the edit distance between “kitten” and 
# “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, 
# and append a “g”.
# Given two strings, compute the edit distance between them.

string1 = "gdsbxgfndf"
string2 = "qefdbefbdbd"
distance = 0
i = 0

while i < min(len(string1), len(string2)):
    if string1[i:i+1] != string2[i:i+1]:
        distance += 1
    if i == len(string1)-1 and len(string1) < len(string2):
        distance += len(string2[i+1:])
    elif i == len(string2)-1 and len(string2) < len(string1):
        distance += len(string1[i+1:])
    i += 1
       
print(distance)