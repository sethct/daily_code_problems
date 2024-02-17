#| We can determine how "out of order" an array A is by counting the number of inversions it has.
#| Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j.
#| That is, a smaller element appears after a larger element.
#| Given an array, count the number of inversions it has. Do this faster than O(N^2) time.
#| You may assume each element in the array is distinct.
#| For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions:
#| (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair
#| forms an inversion.


#-----------------#
# Define Function #
#-----------------#


def merge_sort(arr):
    #| Base case: if the array is of length 0 or 1, it's already sorted
    if len(arr) <= 1:
        return arr, 0
    else:
        #| Divide the array into two halves
        mid = len(arr) // 2
        left_half, left_inversions = merge_sort(arr[:mid])
        right_half, right_inversions = merge_sort(arr[mid:])

        #| Merge the two halves and count inversions
        merged_array, split_inversions = merge_and_count(left_half, right_half)

        #| The total number of inversions is the sum of inversions in left,
        #| right, and those counted during the merge step
        total_inversions = left_inversions + right_inversions + split_inversions

        return merged_array, total_inversions

def merge_and_count(left, right):
    merged = []
    i = j = 0
    inversions = 0

    #| Merge the two arrays and count inversions
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            #| Since left[i] > right[j] and elements in left are before those in right,
            #| each element remaining in left[] will form an inversion with right[j]
            merged.append(right[j])
            inversions += (len(left) - i)
            j += 1

    #| Append any remaining elements to the merged array
    merged += left[i:]
    merged += right[j:]

    return merged, inversions

def count_inversions(arr):
    _, total_inversions = merge_sort(arr)
    return total_inversions

#------------------#
# Test Application #
#------------------#

arr = [2, 4, 1, 3, 5]
print(count_inversions(arr))  # Output: 3

arr = [5, 4, 3, 2, 1]
print(count_inversions(arr))  # Output: 10
