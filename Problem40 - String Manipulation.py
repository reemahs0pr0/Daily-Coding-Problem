# Given a string s and an integer k, break up the string into multiple lines 
# such that each line has a length of k or less. You must break it up so that 
# words don't break across lines. Each line has to have the maximum possible 
# amount of words. If there's no way to break the text up, then return null.
# You can assume that there are no spaces at the ends of the string and that 
# there is exactly one space between each word.
# For example, given the string "the quick brown fox jumps over the lazy dog" 
# and k = 10, you should return: ["the quick", "brown fox", "jumps over", 
# "the lazy", "dog"]. No string in the list has a length of more than 10.

string = "the quick brown fox jumps over the lazy dog" 
k = 43

def my_function(string, k):
    temp_result = []
    result = []
    words = string.split(" ")
    count = 0
    for word in words:
        if len(word) <= k-(count):
            temp_result.append(word)
            count += len(word) + 1
        else:
            result.append(" ".join(temp_result))
            temp_result.clear()
            temp_result.append(word)
            count = len(word) + 1
            if count-1 > k:
                return None
    result.append(" ".join(temp_result))
    return result
    
print(my_function(string, k))