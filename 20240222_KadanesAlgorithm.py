#| Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
#| For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137,
#| since we would take elements 42, 14, -5, and 86.
#| Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.
#| Do this in O(N) time.

#-----------------#
# Define Function #
#-----------------#

def max_subarray_sum(arr):
    #| Initialise the maximum sum found so far and the maximum sum ending here (for the current subarray).
    max_so_far = 0
    max_ending_here = 0
    
    #| Loop through each element in the array.
    for i in arr:
        #| Add the current element to the max_ending_here.
        #| Extend the current subarray to include the current element.
        max_ending_here = max_ending_here + i
        
        #| If adding the current element made the sum negative,
        #| start a new subarray from the next element.
        #| reset max_ending_here to 0.
        if max_ending_here < 0:
            max_ending_here = 0
        
        #| Update max_so_far if the sum of the current subarray (max_ending_here)
        #| is greater than the previous maximum sum found.
        elif (max_so_far < max_ending_here):
            max_so_far = max_ending_here
            
    #| Return the maximum sum found among all subarrays.
    return max_so_far

#------------------#
# Test Application #
#------------------#

arr1 = [34, -50, 42, 14, -5, 86]
print(max_subarray_sum(arr1))  # Output: 137

arr2 = [-5, -1, -8, -9]
print(max_subarray_sum(arr2))  # Output: 0
