# Let user enter the number of timing(s) to compare in HH:mm:ss format. There is no need to validate if the input is in the correct format. Assume all inputs are in correct format. Return the smallest timing entered by the user.

count = int(input("How many timing(s) you want to compare? "))
smallest = None
result = None
for i in range(count):
    timing = input("Enter time " + str(i+1) + " in HH:mm:ss format: ")
    split = timing.split(":")
    hour = int(split[0])
    minute = int(split[1])
    second = int(split[2])
    timing_in_second = hour*3600 + minute*60 + second
    if (smallest == None or timing_in_second < smallest):
        smallest = timing_in_second
        result = timing
print(result)