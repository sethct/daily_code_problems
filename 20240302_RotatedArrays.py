#| An sorted array of integers was rotated an unknown number of times.
#| Given such an array, find the index of the element in the array in
#| faster than linear time. If the element doesn't exist in the array, return null.
#| For example, given the array [13, 18, 25, 2, 8, 10] and the element 8,
#| return 4 (the index of 8 in the array).

#------------------#
# Define Functions #
#------------------#

def search_rotated_array(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        # Check if the left half is sorted
        if arr[left] <= arr[mid]:
            # Check if target is in the left half
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # The right half must be sorted
            # Check if target is in the right half
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    # If the element was not found
    return None

# Example usage
arr = [13, 18, 25, 2, 8, 10]
target = 8
print(search_rotated_array(arr, target))  # Output: 4
