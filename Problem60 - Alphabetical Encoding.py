# Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....
# Given a column number, return its alphabetical column id. For example, given 1, return "A". Given 27, return "AA".

column_number = int(input("Enter column number: "))
result = []
if column_number <= 0:
    print("Invalid column number!")
while (column_number > 0):
    remainder = column_number % 26 if column_number % 26 != 0 else 26
    result.insert(0, chr(remainder+64))
    column_number = column_number // 26
    if remainder == 26:
        column_number -= 1
print(''.join(result))