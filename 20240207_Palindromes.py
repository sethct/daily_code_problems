#| Given a string, find the palindrome that can be made by inserting the fewest
#| number of characters as possible anywhere in the word. If there is more than
#| one palindrome of minimum length that can be made, return the lexicographically
#| earliest one (the first one alphabetically).
#| For example, given the string "race", you should return "ecarace", since we can
#| add three letters to it (which is the smallest amount to make a palindrome). 
#| There are seven other palindromes that can be made from "race" by adding three
#| letters, but "ecarace" comes first alphabetically.

#-----------------#
# Define Function #
#-----------------#

def find_min_insertions_palindrome(s):
    n = len(s)
    # Create a table to store results of subproblems
    dp = [[0 for x in range(n)]for y in range(n)]
    
    # Fill the table
    for gap in range(1, n):
        l = 0
        for r in range(gap, n):
            if s[l] == s[r]:
                dp[l][r] = dp[l+1][r-1]
            else:
                dp[l][r] = min(dp[l+1][r], dp[l][r-1]) + 1
            l += 1
    
    # Reconstruct palindrome
    res = [""] * (n + dp[0][n-1])
    i, j = 0, n-1
    left, right = 0, len(res) - 1
    while i <= j:
        if s[i] == s[j]:
            res[left] = s[i]
            res[right] = s[j]
            i += 1
            j -= 1
        elif dp[i][j-1] < dp[i+1][j]:
            # Insert s[j] at the beginning
            res[left] = s[j]
            res[right] = s[j]
            j -= 1
        else:
            # Insert s[i] at the end
            res[left] = s[i]
            res[right] = s[i]
            i += 1
        left += 1
        right -= 1

    return "".join(res)

# Example usage
s = "race"
print(find_min_insertions_palindrome(s))
