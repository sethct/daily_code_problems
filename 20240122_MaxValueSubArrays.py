#| Given an array of integers and a number k, where 1 <= k <= length of the array,
#| compute the maximum values of each subarray of length k.
#| Do this in O(n) time and O(k) space.
#| You can modify the input array in-place and you do not need to store the results.
#| You can simply print them out as you compute them.

#| Import packages
from collections import deque

#-----------------#
# Define Function #
#-----------------#

def max_values_subarrays(arr, k):
    #| Check for invalid input
    if not arr or k <= 0:
        return

    #| Initialise a deque to store indices of elements in the current window
    dq = deque()

    #| Process the first window and initialise the deque
    for i in range(k):
        #| Remove elements from the rear of the deque if they are smaller than the current element
        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()
        #| Add the current index to the deque
        dq.append(i)

    #| Process the remaining windows
    for i in range(k, len(arr)):
        #| Print the maximum value of the current window (front of the deque)
        print(arr[dq[0]])

        #| Remove elements outside the current window from the front of the deque
        while dq and dq[0] <= i - k:
            dq.popleft()

        #| Remove smaller elements from the rear of the deque
        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()

        #| Add the current index to the deque
        dq.append(i)

    #| Print the maximum value of the last window
    print(arr[dq[0]])

#------------------#
# Test Application #
#------------------#

array = [10, 5, 2, 7, 8, 7]
k = 3
max_values_subarrays(array, k)
