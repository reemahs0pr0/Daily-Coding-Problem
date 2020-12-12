# Given an array of time intervals (start, end) for classroom lectures 
# (possibly overlapping), find the minimum number of rooms required.
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

def overlap(tup1, tup2):
    if tup2[1] < tup1[0] or tup2[0] > tup1[1]:
        return False
    return True

arr = [(30, 75), (0, 50), (60, 150), (45, 65), (100, 200), (0, 100), 
       (65, 200), (90, 170), (5, 60), (75, 100), (0, 70), (80, 90), 
       (0, 40), (70, 80), (70, 75), (110, 190), (50, 150), (150, 160)]
min_room = 0
rooms = []

for i in range(len(arr)):
    add_room = True
    if i == 0:
        rooms.append([arr[i]])
        min_room += 1
    else:
        for j in range(min_room):
            for k in range(len(rooms[j])):
                if overlap(arr[i], rooms[j][k]):
                    break
                if k == len(rooms[j])-1:
                    rooms[j].append(arr[i])
                    add_room = False
                    break
            if add_room == False:
                break
        if add_room == True:
            rooms.append([arr[i]])
            min_room += 1

print(min_room)