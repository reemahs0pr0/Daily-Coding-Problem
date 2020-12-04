# Given an integer k and a string s, find the length of the longest 
# substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with 
# k distinct characters is "bcb".

def longest_substring(s, k):
    chars = []
    results = []
    substring = ""
    for c in range(len(s)):
        if s[c] in chars:
            chars.remove(s[c])
            chars.append(s[c])
            substring += s[c]
        else:
            if len(chars) != k:
                chars.append(s[c])
                substring += s[c]
            else:
                results, substring = \
                    update_results(results, substring) 
                chars, substring = \
                    update_substring(chars, s[c], substring)
        if c == len(s)-1:
            results, substring = \
                update_results(results, substring)
    return results if len(chars) == k else None

def update_results(results, substring):
    if len(results) == 0:
            results.append(substring)
    else:
        if len(results[0]) == len(substring):
            results.append(substring)
        elif len(substring) > len(results[0]):
            results = []
            results.append(substring)
    return results, substring

def update_substring(chars, char, substring):
    chars.remove(chars[0])
    chars.append(char)
    substring += char
    for i in range(len(substring)-1, -1, -1):
        if substring[i] not in chars:
            substring = substring[i+1:]
            break
    return chars, substring

s = "aaabbbaaaaacd"
k = 5

print(longest_substring(s, k))