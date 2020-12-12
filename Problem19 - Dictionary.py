# Given a dictionary of words and a string made up of those words 
# (no spaces), return the original sentence in a list. If there is more than 
# one possible reconstruction, return any of them. If there is no possible 
# reconstruction, then return null.
# For example, given the set of words 'quick', 'brown', 'the', 'fox', and 
# the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 
# 'fox'].
# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the 
# string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] 
# or ['bedbath', 'and', 'beyond'].

dict1 = { 0: 'quick', 1: 'brown', 2: 'the', 3: 'fox'}
dict2 = { 0: 'bed', 1: 'bath', 2: 'bedbath', 3: 'and', 4: 'beyond'}

string1 = "thequickbrownfox"
string2 = "bedbathandbeyond"

def myFunction(s, d):
    l = []
    j = 0
    for i in range(1, len(s)+1):
        if s[j:i] in d.values():
            l.append(s[j:i])
            j = i
    if len(l) == 0:
        return None
    return l
          
print(myFunction(string1, dict1)) 
print(myFunction(string2, dict2))  
print(myFunction(string2, dict1))   