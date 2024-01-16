#| There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
#| Given N, write a function that returns the number of unique ways you can climb the staircase.
#| The order of the steps matters.

#-----------------#
# Define Function #
#-----------------#

def climb_stairs(n):
    #| Base cases: There is 1 way to reach 0th and 1st steps
    if n == 0 or n == 1:
        return 1

    #| Initialise an array to store the number of ways to reach each step
    ways = [0] * (n + 1)

    #| There is 1 way to reach the 0th and 1st steps
    ways[0] = ways[1] = 1

    #| Calculate the number of ways for each step starting from the 2nd step
    for i in range(2, n + 1):
        #| The number of ways to reach the current step is the sum of ways to reach the previous two steps
        ways[i] = ways[i - 1] + ways[i - 2]

    #| The result is the number of ways to reach the last step (n)
    return ways[n]

#------------------#
# Test Application #
#------------------#

N = 4
result = climb_stairs(N)
print(f"There are {result} unique ways to climb {N} steps.")

#----------#
# Part Two #
#----------#

def climb_stairs_variable_steps(n, steps):
    #| Base case: There is 1 way to reach 0th step
    ways = [0] * (n + 1)
    ways[0] = 1

    #| Calculate the number of ways for each step starting from 1st step to nth step
    for i in range(1, n + 1):
        #| For each step, calculate the number of ways by considering each possible step size
        for step in steps:
            if i - step >= 0:
                ways[i] += ways[i - step]

    #| The result is the number of ways to reach the last step (n)
    return ways[n]

#| Example usage:
N = 5
X = {1, 3, 5}
result = climb_stairs_variable_steps(N, X)
print(f"There are {result} unique ways to climb {N} steps with steps {X}.")

