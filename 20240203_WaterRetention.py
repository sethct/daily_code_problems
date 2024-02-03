#| You are given an array of non-negative integers that represents a two-dimensional
#| elevation map where each element is unit-width wall and the integer is the height.
#| Suppose it will rain and all spots between two walls get filled up.
#| Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
#| For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
#| Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second,
#| and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.

#-----------------#
# Define Function #
#-----------------#

def trap_water(heights):
    #| Initialise two pointers for scanning the heights from both ends.
    left, right = 0, len(heights) - 1
    #| Initialise variables to keep track of the max height seen from the left and right.
    left_max, right_max = 0, 0
    #| Initialise a variable to accumulate the total amount of trapped water.
    trapped_water = 0

    #| Loop until the two pointers meet in the middle.
    while left < right:
        #| If the current left height is less than the current right height,
        #| there's potential for trapping water on the left side.
        if heights[left] < heights[right]:
            #| If the current left height is greater than or equal to the max left height seen so far,
            #| update the left max height to the current height.
            if heights[left] >= left_max:
                left_max = heights[left]
            else:
                #| If the current left height is less than the max left height seen so far,
                #| calculate the trapped water at this point and add it to the total.
                #| Subtract the current height from the max left height.
                trapped_water += left_max - heights[left]
            #| Move the left pointer one step to the right.
            left += 1
        else:
            #| If the current right height is greater than or equal to the max right height seen so far,
            #| update the right max height to the current height.
            if heights[right] >= right_max:
                right_max = heights[right]
            else:
                #| If the current right height is less than the max right height seen so far,
                #| calculate the trapped water at this point and add it to the total.
                #| Subtract the current height from the max right height.
                trapped_water += right_max - heights[right]
            #| Move the right pointer one step to the left.
            right -= 1

    #| Return the total amount of trapped water after scanning the entire array.
    return trapped_water

#------------------#
# Test Applicaiton #
#------------------#
print(trap_water([2, 1, 2]))  # Output: 1, illustrating that 1 unit of water is trapped.
print(trap_water([3, 0, 1, 3, 0, 5]))  # Output: 8, illustrating that 8 units of water are trapped.
