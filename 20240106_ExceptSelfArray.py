#| Given an array of integers, return a new array such that each element at
#| index i of the new array is the product of all of the numbers in the
#| original array except the one a i.

#-----------------#
# Define Function #
#-----------------#

def except_self(nums):
    #| Create an array to store the results
    result = [1] * len(nums)

    #| Calculate the product of all elements left of the index
    left_product = 1
    for i in range(len(nums)):
        #| Multiple the result by the products of elements to the left
        #| *= is shorthand for performing multiplication and assignment. 
        #| It multplies the value of x by the value of y and assigns back to x.
        result[i] *= left_product
        #| Update the product of elements to the left
        left_product  *= nums[i]
    
    #| Calculate the product of all elements to the right of each index
    right_product = 1
    #| 1st -1 is starting value, 2nd -1 is end value, 3rd -1 is the step.
    for i in range(len(nums) - 1, -1, -1):
        #| Multiply result by the product of elements to the right
        result[i] *= right_product
        #| Update the product of elements to the right
        right_product *= nums[i]

    return result

#-----------------#
# Test Aplication #
#-----------------#

#| Specify problem input
given_input = [1, 2, 3, 4, 5]

#| Apply function for output
answer = except_self(given_input)

#| Print output
print(answer)