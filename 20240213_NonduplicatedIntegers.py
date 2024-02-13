#| Given an array of integers where every integer occurs three times except for one integer, 
#| which only occurs once, find and return the non-duplicated integer.
#| For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.
#| Do this in O(N) time and O(1) space.

#-----------------#
# Define Function #
#-----------------#

def find_single_number(nums):
    #| Initialise an array of 32 zeros, one for each possible bit position.
    bit_count = [0] * 32
    
    #| Iterate over each number in the input array.
    for num in nums:
        #| For each number, check each of the 32 bit positions.
        for i in range(32):
            #| Use a bit mask to isolate the bit at position i.
            #| The mask is obtained by left shifting 1 by i places.
            bit_mask = 1 << i
            
            #| If the bit at position i in the current number is set (i.e., it's 1),
            #| increment the count for this bit position.
            if num & bit_mask:
                bit_count[i] += 1
                
    #| Reconstruct the single number from its bits. Initially, the result is 0.
    result = 0
    
    #| Define a base value which to add the bit value back to the result if the bit count modulo 3 is not 0.
    #| This reconstructs the unique number bit by bit.
    for i in range(32):
        #| If the bit count for position i modulo 3 is not zero,
        #| it means this bit belongs to the number that appears once.
        if bit_count[i] % 3:
            #| Add this bit to the result.
            #| Shift 1 left by i positions to
            #| set this bit in the result.
            result |= 1 << i
            
    #| If the result is greater than 2^31, then it's a negative number.
    #| Adjust the result accordingly to ensure it's interpreted correctly.
    if result >= 2**31:
        result -= 2**32
    
    return result

# Test the function
print(find_single_number([6, 1, 3, 3, 3, 6, 6]))  # Output: 1
print(find_single_number([13, 19, 13, 13]))      # Output: 19
