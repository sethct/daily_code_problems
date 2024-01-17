#| Given an integer k and a string s, find the length of the longest substring
#| that contains at most k distinct characters.

#------------------#
# Define Substring #
#------------------#

def longest_substring(s, k):
    #| Check if k is 0, in which case there are no distinct characters.
    if k == 0:
        return 0

    #| Dictionary to store the count of each character in the current window.
    char_count = {}

    #| Start and end indices of the sliding window.
    start = 0

    #| Variable to store the maximum length of substring with at most k distinct characters.
    max_length = 0

    #| Loop through the characters in the string.
    for end in range(len(s)):
        char = s[end]
        
        #| Update the count of the current character in the window.
        char_count[char] = char_count.get(char, 0) + 1

        #| Check if the number of distinct characters in the window exceeds k.
        while len(char_count) > k:
            #| Move the start index and update the counts accordingly.
            left_char = s[start]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            start += 1

        #| Update the maximum length of substring.
        max_length = max(max_length, end - start + 1)

    # Return the final result.
    return max_length

#------------------#
# Test Application #
#------------------#

k = 2
s = "eceba"
result = longest_substring_with_k_distinct(s, k)
print(result)  # Output: 3
