# Write an algorithm to justify text. Given a sequence of words and an 
# integer line length k, return a list of strings which represents each 
# line, fully justified.
# More specifically, you should have as many words as possible in each line. 
# There should be at least one space between each word. Pad extra spaces when
# necessary so that each line has exactly length k. Spaces should be 
# distributed as equally as possible, with the extra spaces, if any, 
# distributed starting from the left.
# If you can only fit one word on a line, then you should pad the right-hand 
# side with spaces.
# Each word is guaranteed not to be longer than k.
# For example, given the list of words ["the", "quick", "brown", "fox", 
# "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the 
# following:
# ["the  quick brown", # 1 extra space on the left
# "fox  jumps  over", # 2 extra spaces distributed evenly
# "the   lazy   dog"] # 3 extra spaces distributed evenly

def justify(arr, spaces):
    to_fill = len(arr) - 1
    if to_fill == 0:
        print(arr[0] + " " * spaces)
    else:
        minimum = int(spaces/to_fill)
        extra = spaces%to_fill
        space_arr = []
        for i in range(to_fill):
            if extra != 0:
                space_arr.append(minimum+1)
                extra -= 1
            else:
                space_arr.append(minimum)
            print(arr[i] + " " * space_arr[i], end="")
        print(arr[len(arr)-1])   
    
arr = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
k = 16
length = len(arr[0])
start = 0

for j in range(1, len(arr)):
    length += 1 + len(arr[j])
    if length > k:
        justify(arr[start:j], k-(length-(len(arr[start:j])-1)-(1+len(arr[j]))))
        length = len(arr[j])
        start = j
    if j == len(arr)-1:
        justify(arr[start:j+1], k-(length-(len(arr[start:j+1])-1)))