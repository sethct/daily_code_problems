#| Return a new sorted merged list from K sorted lists, each with size N

import heapq

def merge_sorted_lists(lists):
    #| Create result list to store merged sorted elements
    result = []
    #| Min heap to efficiently track smallest element from each list
    heap = []

    #| Initialise the heap with the first element from each list along with list and element index
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    while heap:
        #| Pop the smallest element from the heap
        val, list_idx, elem_idx = heapq.heappop(heap)
        #| Add the smallest element to the result list
        result.append(val)

        #| Move to the next element in the same list
        if elem_idx + 1 < len(lists[list_idx]):
            heapq.heappush(heap, (lists[list_idx][elem_idx + 1], list_idx, elem_idx + 1))

    return result

#---------------#
# Example Usage #
#---------------#

#| Number of sorted lists
K = 3

#| Size of each sorted list
N = 4

#| Generate some example sorted lists
lists = [sorted(range(i, i + N)) for i in range(0, K * N, N)]

#| Call function
merged_list = merge_sorted_lists(lists)