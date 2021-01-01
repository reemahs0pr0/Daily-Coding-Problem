# Given an unordered list of flights taken by someone, each represented 
# as (origin, destination) pairs, and a starting airport, compute the 
# person's itinerary. If no such itinerary exists, return null. If there 
# are multiple possible itineraries, return the lexicographically 
# smallest one. All flights must be used in the itinerary.
# For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), 
# ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should 
# return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].
# Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting 
# airport 'COM', you should return null.
# Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] 
# and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 
# 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. 
# However, the first one is lexicographically smaller.

from Quicksort import quicksort

def create_graph(arr):
    graph = {}
    for tup in arr:
        if tup[0] not in graph:
            graph[tup[0]] = []
            graph[tup[0]].append(tup[1])
        else:
            graph[tup[0]].append(tup[1])
    return graph

def dfs(graph, start, visited = None, count=0):
    global length
    if visited is None:
        visited = []
    if start not in graph:
        return
    for vertex in graph[start]:
        if len(visited) > 0:
            prev_flight = visited[len(visited)-1]
            prev_dest = prev_flight[1]
            if prev_dest != start:
                return
        if (start, vertex) not in visited:
            visited.append((start, vertex))
            count += 1
            if count == length:
                print_itinery(visited)
                return
            else:
                dfs(graph, vertex, visited, count)
            
def print_itinery(flights):
    global valid
    valid = True
    itinery = []
    for i in range(len(flights)):
        itinery.append(flights[i][0])
        if i == len(flights) -1:
            itinery.append(flights[i][1])
    print(itinery)
    
def compute_itinery(graph, start):
    dfs(graph, start)
    if valid == False:
        print('Invalid inventory')
            
arr = [('SFO', 'COM'), ('COM', 'YYZ')]
length = len(arr)
quicksort(arr, 0, length-1)
graph = create_graph(arr)
start = 'SFO'
valid = False
compute_itinery(graph, start)