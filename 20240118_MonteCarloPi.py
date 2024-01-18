#| The area of a circle is defined as πr^2.
#| Estimate π to 3 decimal places using a Monte Carlo method.

#| Import required packages
import random

#-----------------#
# Define Function #
#-----------------#

def estimate_pi(num_samples):
    #| Initialise a counter for points inside the quarter circle
    inside_circle = 0

    #| Iterate through the specified number of random points
    for _ in range(num_samples):
        #| Generate random coordinates (x, y) within the unit square
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        #| Calculate the distance from the origin (0,0)
        distance = x**2 + y**2

        #| Check if the point is inside the quarter circle (distance <= 1)
        if distance <= 1:
            inside_circle += 1

    #| The ratio of points inside the quarter circle to the total points
    #| is proportional to the ratio of the areas of the quarter circle to the square.
    #| Multiply by 4 to estimate the value of π.
    return (inside_circle / num_samples) * 4

#------------------#
# Test Application #
#------------------#

#| Set the number of samples for the Monte Carlo simulation
num_samples = 1000000

#| Estimate π using the Monte Carlo method
pi_estimate = estimate_pi(num_samples)

#| Print the result
print(f"Estimated π: {pi_estimate:.3f}")
