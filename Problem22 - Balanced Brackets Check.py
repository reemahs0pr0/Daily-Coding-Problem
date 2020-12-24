# Given a string of round, curly, and square open and closing brackets, 
# return whether the brackets are balanced (well-formed).
# For example, given the string "([])[]({})", you should return true.
# Given the string "([)]" or "((()", you should return false.

string1 = "([])[]({})"
string2 = "([)]"
string3 = "((()"

def check(string):
    open_set = {"(", "{", "["}
    checklist = []
    for c in string:
        if len(checklist) == 0 or c in open_set:
            checklist.append(c)
        else:
            if checklist[len(checklist)-1] == "(" and c == ")":
                del checklist[-1]
            elif checklist[len(checklist)-1] == "[" and c == "]":
                del checklist[-1]
            elif checklist[len(checklist)-1] == "{" and c == "}":
                del checklist[-1]
            else:
                return False
    if len(checklist) == 0:
        return True
    return False

print(check(string1))
print(check(string2))
print(check(string3))