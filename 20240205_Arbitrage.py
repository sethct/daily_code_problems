#| Suppose you are given a table of currency exchange rates, represented as a 2D array.
#| Determine whether there is a possible arbitrage: that is, whether there is some sequence
#| of trades you can make, starting with some amount A of any currency, so that you can end
#| up with some amount greater than A of that currency.
#| There are no transaction costs and you can trade fractional quantities.

import math

#-----------------#
# Define Function #
#-----------------#

import math

def find_arbitrage(currency_matrix):
    #| The function takes a 2D array named currency_matrix as input
    #| where each element in the array represents the exchange rate
    #| from one currency to another.

    #| Transform the matrix by taking the negative logarithm of each exchange rate.
    transformed_graph = [[-math.log(edge) for edge in row] for row in currency_matrix]

    #| Number of currencies in the matrix
    n = len(currency_matrix)

    #| Initialise a list to keep track of the minimum "distance" from a starting currency
    #| to each other currency.
    #| Initially, set all distances to infinity to signify that they haven't been visited/updated.
    distance = [float('inf')] * n
    distance[0] = 0  # Set the distance to the starting currency to 0.

    #| Update distance to a nide if shorter path found for all edges n-1 times.
    #| Update the cumulative negative log of exchange rates if a better (lower) value is found.
    for _ in range(n - 1):
        for source in range(n):
            for dest in range(n):
                if distance[source] + transformed_graph[source][dest] < distance[dest]:
                    distance[dest] = distance[source] + transformed_graph[source][dest]

    #| After relaxing all edges n-1 times, a final pass is done to check for negative cycles.
    #| A negative cycle would indicate that further reductions in "distance" are possible,
    #| which translates to an arbitrage opportunity in this context.
    for source in range(n):
        for dest in range(n):
            if distance[source] + transformed_graph[source][dest] < distance[dest]:
                # If distance can still be reduced, a negative cycle exists.
                return True  # Arbitrage opportunity detected

    #| If no negative cycles are detected, there are no arbitrage opportunities.
    return False

#------------------#
# Test Application #
#------------------#

currency_matrix = [
    [1,     0.739, 0.657, 0.014],
    [1.353, 1,     0.889, 0.019],
    [1.522, 1.125, 1,     0.021],
    [70.74, 53.23, 47.68, 1    ],
]

print(find_arbitrage(currency_matrix))
