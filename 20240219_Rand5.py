#| Using a function rand5() that returns an integer from 1 to 5 (inclusive)
#| with uniform probability, implement a function rand7() that returns an
#| integer from 1 to 7 (inclusive).

import random

def rand5():
    return random.randint(1, 5)

def rand7():
    while True:
        # Step 1 and 2: Generate a number from 0 to 24
        num = (rand5() - 1) * 5 + (rand5() - 1)
        
        # Step 3: Reject if the number is outside the range 0 to 20
        if num < 21:
            # Step 4: Map the number from 0 to 6, then shift to 1 to 7
            return num % 7 + 1
