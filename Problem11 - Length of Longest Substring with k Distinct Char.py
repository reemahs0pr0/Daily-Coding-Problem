# Given an integer k and a string s, find the length of the longest 
# substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with 
# k distinct characters is "bcb".

import collections

def longest_substring(s, k):
    chars = collections.deque([])
    results = []
    substring = ""
    for c in range(len(s)):
        if s[c] in chars:
            if chars[len(chars)-1] != s[c]:
                chars.append(s[c])
                if len(chars) == k+1:
                    chars.popleft()
            substring += s[c]
            if c == len(s)-1:
                results, substring = \
                    update_results(results, substring)
        else:
            if len(chars) != k:
                chars.append(s[c])
                substring += s[c]
            else:
                results, substring = \
                    update_results(results, substring)     
                chars.append(s[c])
                chars.popleft()
                substring += s[c]
                for i in range(len(substring)-1, -1, -1):
                    if substring[i] not in chars:
                        substring = substring[i+1:]
                        break
                if c == len(s)-1:
                    results, substring = \
                        update_results(results, substring) 
    return results

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

s = "abcba"
k = 2

print(longest_substring(s, k))