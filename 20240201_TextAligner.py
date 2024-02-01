#| Write an algorithm to justify text. Given a sequence of words and an integer line length k,
#| return a list of strings which represents each line, fully justified.
#| More specifically, you should have as many words as possible in each line.
#| There should be at least one space between each word. Pad extra spaces when necessary so that
#| each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces,
#| if any, distributed starting from the left.
#| If you can only fit one word on a line, then you should pad the right-hand side with spaces.
#| Each word is guaranteed not to be longer than k.

#-----------------#
# Define Function #
#-----------------#

def full_justify(words, maxWidth):
    res, cur, num_of_letters = [], [], 0
    #| res: Final result list, containing fully justified lines as strings.
    #| cur: Current line being processed, a list of words that fit within maxWidth.
    #| num_of_letters: Total length of characters from words added to `cur` (excluding spaces).

    for w in words:
        #| Iterate through each word in the input list.
        if num_of_letters + len(w) + len(cur) > maxWidth:
            #| Check if adding the current word exceeds maxWidth.
            #| len(cur) is used to calculate the minimum required spaces (one space after each word except the last).
            for i in range(maxWidth - num_of_letters):
                #| Distribute extra spaces to make the line exactly maxWidth long.
                #| Spaces are added in a round-robin fashion starting from the left.
                cur[i % (len(cur) - 1 or 1)] += ' '
                #| The modulo operation ensures even distribution of spaces.
                #| "(len(cur) - 1 or 1)" prevents division by zero and handles single-word lines.
            #| Join the words and spaces in `cur` to form a justified line, then add it to `res`.
            res.append(''.join(cur))
            #| Reset `cur` and `num_of_letters` for the next line.
            cur, num_of_letters = [], 0

        #| Add the current word to the current line.
        cur += [w]
       #| Update the total number of letters (excluding spaces) for the current line.
        num_of_letters += len(w)

    #| Handle the last line: it should be left-justified and spaces added to the end.
    #| ' '.join(cur) creates a string with one space between words.
    #| .ljust(maxWidth) ensures the line is exactly maxWidth characters by adding spaces to the end.
    return res + [' '.join(cur).ljust(maxWidth)]

#| This function wraps the full_justify function for a cleaner interface.
def justify_text(words, k):
    #| Call the full_justify function to get the list of justified lines.
    justified_lines = full_justify(words, k)
    #| Return the fully justified text.
    return justified_lines

#---------------#
# Example Usage #
#---------------#

words = ["This", "is", "an", "example", "of", "text", "justification."]
k = 16
justified_text = justify_text(words, k)
#| Justify the example text with a line width of 16 characters.
for line in justified_text:
    #| Print each justified line.
    print(f"'{line}'")
