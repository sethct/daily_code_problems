#| Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list.
#| If there is more than one possible reconstruction, return any of them.
#| If there is no possible reconstruction, then return null.

#| For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
#| you should return ['the', 'quick', 'brown', 'fox'].

#-----------------#
# Define Function #
#-----------------#

def word_break(s, wordDict):
    #| Helper function to check if the string 's' can be segmented into a sequence of words in 'wordDict'.
    def can_break(s, wordDict, memo):
        #| Check if the result for the current string is already computed and stored in 'memo'.
        if s in memo:
            return memo[s]

        #| Base case: If the string is empty, return an empty list.
        if not s:
            return []

        #| Iterate through each word in the dictionary.
        for word in wordDict:
            #| Check if the current string starts with this word.
            if s.startswith(word):
                #| Get the remaining part of the string after removing the current word.
                suffix = s[len(word):]

                #| If the suffix is empty or is a word in the dictionary, construct the result.
                if not suffix or suffix in wordDict:
                    memo[s] = [word] + (can_break(suffix, wordDict, memo) if suffix else [])
                    return memo[s]
                else:
                    #| Recursively check if the remaining string can be segmented.
                    rest = can_break(suffix, wordDict, memo)
                    if rest is not None:
                        #| If it can be segmented, prepend the current word to the result.
                        memo[s] = [word] + rest
                        return memo[s]

        #| If the string cannot be segmented, store None in 'memo' and return None.
        memo[s] = None
        return None

    #| Convert the word dictionary to a set for faster lookups.
    #| Call the helper function with the original string, the set, and an empty memo dictionary.
    return can_break(s, set(wordDict), {})

#------------------#
# Test Application #
#------------------#

words = ['quick', 'brown', 'the', 'fox']
sentence = "thequickbrownfox"
result = word_break(sentence, words)
print(result)