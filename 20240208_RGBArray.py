#| Given an array of strictly the characters 'R', 'G', and 'B',
#| segregate the values of the array so that all the Rs come first,
#| the Gs come second, and the Bs come last.
#| You can only swap elements of the array.
#| Do this in linear time and in-place.

#-----------------#
# Define Function #
#-----------------#

def segregateRGB(arr):
    
    #| Initialise pointers
    low = 0            # Start of the array
    mid = 0            # Current element to check
    high = len(arr) - 1  # End of the array

    #| Iterate through the array
    while mid <= high:
        if arr[mid] == 'R':
            #| Swap the 'R' to the position pointed by 'low'
            #| and move both 'low' and 'mid' pointers forward
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 'G':
            #| If it's 'G', it's already in the correct section
            #| Just move the 'mid' pointer forward
            mid += 1
        else:  # arr[mid] == 'B'
            #| Swap the 'B' to the position pointed by 'high'
            #| and move 'high' pointer backward
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

#------------------#
# Test Application #
#------------------#

arr = ['G', 'B', 'R', 'R', 'B', 'G', 'G']
print("Original array:", arr)
segregateRGB(arr)
print("Segregated array:", arr)
