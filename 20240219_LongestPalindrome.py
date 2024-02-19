#| Given a string, find the longest palindromic contiguous substring.
#| If there are more than one with the maximum length, return any one.
#| For example, the longest palindromic substring of "aabcdcb" is "bcdcb". 
#| The longest palindromic substring of "bananas" is "anana".

#-----------------#
# Define Function #
#-----------------#

def longest_palindromic_substring(s: str) -> str:
    #| Function to expand around the center and find the longest palindrome.
    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        #| Return the longest palindrome for this center.
        return s[left+1:right]

    #| Initialise the longest palindrome as an empty string.
    longest = ""
    for i in range(len(s)):
        #| Check for odd length palindromes.
        odd_palindrome = expand_around_center(i, i)
        #| Check for even length palindromes.
        even_palindrome = expand_around_center(i, i+1)

        #| Update the longest palindrome if a longer one is found.
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        if len(even_palindrome) > len(longest):
            longest = even_palindrome

    return longest

# Example usage
print(longest_palindromic_substring("aabcdcb"))  # Output: "bcdcb"
print(longest_palindromic_substring("bananas"))  # Output: "anana"
