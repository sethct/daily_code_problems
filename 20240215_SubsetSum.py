#| Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k.
#| If such a subset cannot be made, then return null.
#| Integers can appear more than once in the list. You may assume all numbers in the list are positive.
#| For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

#-----------------#
# Define Function #
#-----------------#

def find_subset_to_sum_k(S, k):
    #| Add dictionary to store the results of subproblems
    memo = {}
    
    def dfs(index, current_sum):
        #| If the current sum equals the target, return an empty list
        if current_sum == k:
            return []
        #| If the current sum exceeds the target or have gone through all elements, return None
        if current_sum > k or index >= len(S):
            return None
        
        #| If already computed the result for this state, return it
        if (index, current_sum) in memo:
            return memo[(index, current_sum)]
        
        #| Include the current element and move to the next
        with_current = dfs(index + 1, current_sum + S[index])
        if with_current is not None:
            memo[(index, current_sum)] = [S[index]] + with_current
            return memo[(index, current_sum)]
        
        #| Exclude the current element and move to the next
        without_current = dfs(index + 1, current_sum)
        if without_current is not None:
            memo[(index, current_sum)] = without_current
            return memo[(index, current_sum)]
        
        #| If sum can not be made with the current configuration, remember this to avoid recomputation
        memo[(index, current_sum)] = None
        return None
    
    return dfs(0, 0)

#------------------#
# Test Application #
#------------------#

S = [12, 1, 61, 5, 9, 2]
k = 24
print(find_subset_to_sum_k(S, k))
