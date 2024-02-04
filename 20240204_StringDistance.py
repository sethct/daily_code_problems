#| The edit distance between two strings refers to the minimum number of
#| character insertions, deletions, and substitutions required to change
#| one string to the other. For example, the edit distance between “kitten” 
#| and “sitting” is three: substitute the “k” for “s”, substitute the “e”
#| for “i”, and append a “g”.
#| Given two strings, compute the edit distance between them.

#-----------------#
# Define Function #
#-----------------#

def edit_distance(s1, s2):
    #| Determine the lengths of the strings s1 and s2
    m, n = len(s1), len(s2)
    
    #| Initialise a matrix to store the edit distances
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    #| Initialise the first column of the matrix
    #| This represents the number of operations needed to transform the substring of s1 to an empty string
    for i in range(m+1):
        dp[i][0] = i
    
    #| Initialise the first row of the matrix
    #| This represents the number of operations needed to transform an empty string to the substring of s2
    for j in range(n+1):
        dp[0][j] = j
    
    #| Fill the rest of the matrix
    for i in range(1, m+1):
        for j in range(1, n+1):
            #| Check if the current characters in both strings are the same
            if s1[i-1] == s2[j-1]:
                cost = 0  # No operation needed if the characters are the same
            else:
                cost = 1  # A substitution is needed otherwise
            
            #| The value of the current cell is the minimum of three possible operations:
            #| 1. Deletion: Remove a character from s1 (move from the cell above, dp[i-1][j], and add 1 to the
            #| 2. Insertion: Add a character to s1 to match s2 (move from the cell to the left, dp[i][j-1], and add 1 to the cost)
            #| 3. Substitution: Replace a character in s1 with the matching character in s2 (move diagonally from the cell, dp[i-1][j-1], and add the cost (0 or 1))
            dp[i][j] = min(dp[i-1][j] + 1,  # Deletion
                           dp[i][j-1] + 1,  # Insertion
                           dp[i-1][j-1] + cost)  # Substitution
    
    #| After filling the matrix, the bottom-right cell contains the edit distance
    return dp[m][n]

#------------------#
# Test Application #
#------------------#

s1 = "kitten"
s2 = "sitting"
# Prints the edit distance between the two strings using the function
print(f"The edit distance between '{s1}' and '{s2}' is {edit_distance(s1, s2)}.")