#| Given a function that generates perfectly random numbers between 1 and k (inclusive),
#| where k is an input, write a function that shuffles a deck of cards
#| represented as an array using only swaps.
#| It should run in O(N) time.

import random

#------------------#
# Define Functions #
#------------------#

def rand(k):
    #| Generates a random number between 1 and k (inclusive).
    #| Adjusting it for 0-based indexing used in arrays.
    return random.randint(1, k) - 1

def shuffle_deck(cards):
    n = len(cards)
    for i in range(n-1, 0, -1):
        #| Generate a random index from 0 to i (inclusive)
        j = rand(i+1)
        #| Swap the current element with the element at the random index
        cards[i], cards[j] = cards[j], cards[i]
    return cards

#------------------#
# Test Application #
#------------------#

deck = [i for i in range(1, 53)]  # A deck of cards represented as numbers 1 to 52
shuffled_deck = shuffle_deck(deck)
print(shuffled_deck)
