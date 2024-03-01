#| Given a string s and an integer k, break up the string into multiple lines
#| such that each line has a length of k or less. You must break it up so that
#| words don't break across lines. Each line has to have the maximum possible
#| amount of words. If there's no way to break the text up, then return null.
#| You can assume that there are no spaces at the ends of the string and that
#| there is exactly one space between each word.

#------------------#
# Define Functions #
#------------------#

def break_string(s, k):
    words = s.split(' ')
    lines = []
    current_line = ''

    for word in words:
        #| Check if the current word is longer than k
        if len(word) > k:
            return None

        #| If adding the word to the current line doesn't exceed the limit
        if len(current_line) + len(word) <= k:
            #| If the current line is not empty, add a space before the word
            if current_line:
                current_line += ' ' + word
            else:
                current_line = word
        else:
            #| If adding the word would exceed the limit, start a new line
            lines.append(current_line)
            current_line = word

    #| Add the last line
    if current_line:
        lines.append(current_line)

    return lines

#------------------#
# Test Application #
#------------------#

s = "This is an example of a string that we want to break up"
k = 10
result = break_string(s, k)
if result:
    for line in result:
        print(line)
else:
    print(None)
