# Suppose we represent our file system by a string in the following 
# manner:
# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
# dir
#     subdir1
#     subdir2
#         file.ext
# The directory dir contains an empty sub-directory subdir1 and a 
# sub-directory subdir2 containing a file file.ext.
# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\t
# subsubdir2\n\t\t\tfile2.ext" represents:
# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext
# The directory dir contains two sub-directories subdir1 and subdir2. 
# subdir1 contains a file file1.ext and an empty second-level sub-directory 
# subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 
# containing a file file2.ext.
# We are interested in finding the longest (number of characters) absolute 
# path to a file within our file system. For example, in the second example 
# above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", 
# and its length is 32 (not including the double quotes).
# Given a string representing the file system in the above format, return 
# the length of the longest absolute path to a file in the abstracted file 
# system. If there is no file in the system, return 0.
# Note:
# The name of a file contains at least a period and an extension.
# The name of a directory or sub-directory will not contain a period.

class Node:
    path = ""
    def __init__(self, name, level=1, sub=None):
        self.path = name
        self.sub = sub
        self.level = level
        if name[-4:] == ".ext" and len(self.path) > len(Node.path):
            Node.path = self.path
    def add(self, name, level):
        if self.sub is None or self.sub.level == level:
            self.sub = Node(self.path + "/" + name, level)
        else:
            self.sub.add(name, level)
    def longest_path(self):
        return Node.path

string = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\t\t\tsubsubsubdir1\n\t\t\t\tfile1_1.ext\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print(string)
print()
string = string.replace("\t", " ")
substring_arr = string.split("\n")
name_arr = []
for substring in substring_arr:
    name_arr.append(substring.strip())
           
for i in range(len(substring_arr)):
    current_level = 1
    if i == 0:
        folder = Node(name_arr[i], current_level)
    else:
        for j in range(0, len(substring_arr[i])):
            if substring_arr[i][j] == " ":
                current_level += 1
            else:
                folder.add(name_arr[i], current_level)
                break
            
print(folder.longest_path())    