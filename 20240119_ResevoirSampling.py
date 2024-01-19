#| Given a stream of elements too large to store in memory,
#| pick a random element from the stream with uniform probability.

#| Import relevant packages
import random

#-----------------#
# Define Function #
#-----------------#

#| Build function
def reservoir_sampling(stream):
    #| Initialise variables
    result = None  # Variable to store the selected element
    count = 0      # Variable to keep track of the number of elements processed

    #| Iterate through the stream
    for i, element in enumerate(stream):
        #| For the first 'count + 1' elements, select each one with probability 1/(count + 1)
        if random.randint(0, count) == 0:
            result = element  # Update the result with the current element

        #| Increment the count
        count += 1

    return result  # Return the randomly selected element

#------------------#
# Test Application #
#------------------#

stream = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random_element = reservoir_sampling(stream)

print("Randomly selected element:", random_element)
