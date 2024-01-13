#| Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. 
#| Numbers can be 0 or negative.
#| For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
#| [5, 1, 1, 5] should return 10, since we pick 5 and 5.

#| Define function
def max_sum_non_adjacent(nums):
    #| Check if the input list is empty
    if not nums:
        return 0

    #| Check if the input list has only one element
    if len(nums) == 1:
        return max(0, nums[0])

    #| Initialize an array to store the maximum sum at each index
    max_sum = [0] * len(nums)

    #| Base cases
    max_sum[0] = max(0, nums[0])  # Max sum for the first element
    max_sum[1] = max(max_sum[0], nums[1])  # Max sum for the second element

    #| Fill in the array using dynamic programming
    for i in range(2, len(nums)):
        #| Calculate the maximum sum at each index, considering the two possible cases:
        #| 1. The maximum sum at the previous index (max_sum[i - 1])
        #| 2. The sum of the element at the current index and the maximum sum two indices back (max_sum[i - 2] + nums[i])
        max_sum[i] = max(max_sum[i - 1], max_sum[i - 2] + nums[i])

    #| The final result is the maximum sum at the last index
    return max_sum[-1]

# Example usage:
nums1 = [2, 4, 6, 2, 5]
nums2 = [5, 1, 1, 5]

result1 = max_sum_non_adjacent(nums1)
result2 = max_sum_non_adjacent(nums2)

print(result1)  # Output: 13
print(result2)  # Output: 10
