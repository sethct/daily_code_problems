#| Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs,
#| and a starting airport, compute the person's itinerary. If no such itinerary exists, return null.
#| If there are multiple possible itineraries, return the lexicographically smallest one. All flights
#| must be used in the itinerary.

#| For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
#| and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

#|Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

#|Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A',
#| you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also
#| a valid itinerary. However, the first one is lexicographically smaller.

#-----------------#
# Define Function #
#-----------------#

def find_itinerary(flights, starting_airport):
    #| Create a graph from the flights list, sorting the destinations for each origin
    graph = {}
    for origin, destination in flights:
        if origin in graph:
            graph[origin].append(destination)
        else:
            graph[origin] = [destination]
    for origin in graph:
        graph[origin].sort(reverse=True)  # Sort in reverse for easier pop from the end

    itinerary = []

    def dfs(airport):
        #| Use the destinations from the current airport
        while airport in graph and graph[airport]:
            next_airport = graph[airport].pop()  # Pop ensures the same flight is not revisited
            dfs(next_airport)
        itinerary.append(airport)

    #| Start the DFS from the given starting airport
    dfs(starting_airport)

    #| If all flights are used, return the itinerary in the correct order
    if len(itinerary) == len(flights) + 1:
        return itinerary[::-1]  #| Reverse itinerary to get the correct order
    else:
        return None

# Test the function with the provided examples
flights1 = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
starting_airport1 = 'YUL'
print(find_itinerary(flights1, starting_airport1))