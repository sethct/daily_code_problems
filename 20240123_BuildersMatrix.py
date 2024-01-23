#| A builder is looking to build a row of N houses that can be of K different colors.
#| He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.
#| Given an N by K matrix where the nth row and kth column represents the cost to build the nth house
#| with kth color, return the minimum cost which achieves this goal.

#-----------------#
# Define Function #
#-----------------#

def min_cost(matrix):
    #| Check if the input matrix is empty
    if not matrix or len(matrix) == 0:
        return 0

    #| Get the number of houses (n) and colors (k)
    n, k = len(matrix), len(matrix[0])

    #| Create a DP table to store the minimum cost at each house and color
    dp = [[0] * k for _ in range(n)]

    #| Initialise the first row with the costs of the first house
    dp[0] = matrix[0]

    #| Iterate through the houses
    for i in range(1, n):
        for j in range(k):
            #| Calculate the minimum cost for the current house and color
            #| by adding the cost of the current color and the minimum cost
            #| from the previous row, excluding the cost of the current color
            dp[i][j] = matrix[i][j] + min(dp[i - 1][:j] + dp[i - 1][j + 1:])

    #| Return the minimum cost from the last row
    return min(dp[-1])

#------------------#
# Test Application #
#------------------#

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = min_cost(matrix)
print(result)
