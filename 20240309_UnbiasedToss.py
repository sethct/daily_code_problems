#| Assume you have access to a function toss_biased() which returns 0 or 1
#| with a probability that's not 50-50 (but also not 0-100 or 100-0).
#| You do not know the bias of the coin.
#| Write a function to simulate an unbiased coin toss.

import random

#------------------#
# Define Functions #
#------------------#

def toss_biased():
    return 0 if random.random() < 0.7 else 1

def toss_unbiased():
    """
    Simulates an unbiased coin toss using the biased toss_biased function.

    Returns:
        int: 0 or 1, with approximately 50-50 probability.
    """
    while True:  # Keep trying until we get a valid sequence.
        first_toss = toss_biased()
        second_toss = toss_biased()
        
        if first_toss != second_toss:
            # We return the first toss because the sequence (first_toss, second_toss)
            # is either (0, 1) or (1, 0), both of which are equally likely.
            return first_toss
        # If we get here, the sequence was either (0, 0) or (1, 1),
        # so we discard it and try again.

#------------------#
# Test Application #
        #------------------#

result = toss_unbiased()
print(f"Unbiased toss result: {result}")
