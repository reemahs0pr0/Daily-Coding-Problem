# Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string. For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7].

def find_pattern(string, pattern):
    result = []
    pattern_length = len(pattern)
    i = 0
    while i < len(string)-(pattern_length-1):
        if (string[i:i+3] == pattern):
            result.append(i)
            i += 3
        i += 1
    print(result)

string = 'abracadabrabcdeabr'
pattern = 'abr'
find_pattern(string, pattern)