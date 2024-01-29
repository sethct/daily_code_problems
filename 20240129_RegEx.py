#| Implement regular expression matching with the following special characters:
#| . (period) which matches any single character
#| * (asterisk) which matches zero or more of the preceding element
#| That is, implement a function that takes in a string and a valid regular expression
#| and returns whether or not the string matches the regular expression.

def is_match(text, pattern):
    #| Base case: If both text and pattern are empty, it's a match
    if not pattern:
        return not text

    #| Check the first character match (taking into account the '.' wildcard)
    first_match = bool(text) and pattern[0] in {text[0], '.'}

    #| If the pattern has a '*' as the second character
    if len(pattern) >= 2 and pattern[1] == '*':
        #| Proceed in one of two ways:
        #| 1. Skip the '*' and the character before it in the pattern
        #| 2. If first character of the string matches the first character of the pattern, 
        #|    try matching the rest of the string with the same pattern
        return (is_match(text, pattern[2:]) or
                first_match and is_match(text[1:], pattern))
    else:
        #| If the pattern does not have a '*' as the second character, 
        #| just move to the next character in both the string and the pattern
        return first_match and is_match(text[1:], pattern[1:])
