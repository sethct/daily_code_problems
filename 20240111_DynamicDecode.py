#| Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
#| For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
#| You can assume that the messages are decodable. For example, '001' is not allowed.

def num_decode(s):
    #| Get the length of the input string
    n = len(s)

    #| Check for edge cases
    if n == 0:
        return 0
    if s[0] == '0':
        return 0

    #| Initialize an array to store the number of ways to decode substrings
    dp = [0] * (n + 1)
    dp[0] = 1  # There is one way to decode an empty string
    dp[1] = 1  # There is one way to decode a string of length 1

    # Iterate through the string starting from the second character
    for i in range(2, n + 1):
        # If the current digit is not '0', add the number of ways from the previous digit
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]

        # If the current and previous digits form a valid mapping (10 to 26), add the ways from two steps back
        two_digit = int(s[i - 2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]

    # The final element in the dp array represents the number of ways to decode the entire string
    return dp[n]

#-------------#
# Application #
#-------------#

#| Define message
encoded_message = '111'

#| Apply Function
result = num_decode(encoded_message)
print(result)  # Output: 3