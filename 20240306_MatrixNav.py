#| There is an N by M matrix of zeroes. Given N and M, write a function to count
#| the number of ways of starting at the top-left corner and getting to the bottom-right
#| corner. You can only move right or down.
#| For example, given a 2 by 2 matrix, you should return 2, since there are two ways to
#| get to the bottom-right:
#| Right, then down
#| Down, then right
#| Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.


#------------------#
# Define Functions #
#------------------#

def count_ways(N, M):
    # Create a 2D array (N x M) filled with 0s
    dp = [[0]*M for _ in range(N)]
    
    # Fill the first row and first column with 1s
    # since there's only one way to reach any cell in the first row or first column
    for i in range(N):
        dp[i][0] = 1
    for j in range(M):
        dp[0][j] = 1
    
    # Fill the rest of the dp table
    for i in range(1, N):
        for j in range(1, M):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    # The bottom-right corner will have the total number of ways
    return dp[-1][-1]

#------------------#
# Test Application #
#------------------#

print(count_ways(2, 2))  # Output: 2
print(count_ways(5, 5))  # Output: 70
