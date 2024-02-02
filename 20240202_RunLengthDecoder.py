#| Run-length encoding is a fast and simple method of encoding strings.
#| The basic idea is to represent repeated successive characters as a single count and character.
#| For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

#| Implement run-length encoding and decoding. You can assume the string to be encoded have no digits
#| and consists solely of alphabetic characters. You can assume the string to be decoded is valid.

#-----------------#
# Define Funciton #
#-----------------#

def run_length_encode(s):
    """
    Encodes the input string using run-length encoding.
    :param s: The input string to be encoded.
    :return: The run-length encoded string.
    """
    #| If the input string is empty, return an empty string.
    if not s:
        return ""

    #| Initialize an empty list to store the encoded parts.
    encoded = []
    #| Start with the first character of the string.
    current_char = s[0]
    #| Initialize the count of the current character.
    count = 1

    #| Iterate over the string starting from the second character.
    for char in s[1:]:
        if char == current_char:
            #| If the current character matches the previous, increment the count.
            count += 1
        else:
            #| Append the count and character to the list.
            encoded.append(f"{count}{current_char}")
            #| Update the current character.
            current_char = char
            #| Reset the count for the new character.
            count = 1
    #| Append the last character and its count.
    encoded.append(f"{count}{current_char}")

    #| Join the encoded parts into a single string and return it.
    return ''.join(encoded)

def run_length_decode(s):
    """
    Decodes a run-length encoded string.
    :param s: The run-length encoded string to be decoded.
    :return: The decoded original string.
    """
    #| Initialise an empty list to store the decoded characters.
    decoded = []
    #| Initialise an empty string to build up the count.
    count = ""

    for char in s:
        if char.isdigit():
            #| If the character is a digit, add it to the count string.
            count += char
        else:
            #| Repeat the character 'count' times and append to the list.
            decoded.append(char * int(count))
            #| Reset count for the next character.
            count = ""

    #| Join the decoded parts into a single string and return it.
    return ''.join(decoded)

