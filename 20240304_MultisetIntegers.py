#| Given a multiset of integers, return whether it can be partitioned
#| into two subsets whose sums are the same.
#| For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it
#|  would return true, since we can split it up into {15, 5, 10,
#| 15, 10} and {20, 35}, which both add up to 55.
#| Given the multiset {15, 5, 20, 10, 35}, it would return false,
#| since we can't split it up into two subsets that add up to the same sum.

#------------------#
# Define Functions #
#------------------#

def canPartition(nums):
    total_sum = sum(nums)
    # If total_sum is odd, it cannot be partitioned into two equal subsets
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    
    # Initialize: It's possible to make sum 0 with 0 elements
    for i in range(n + 1):
        dp[i][0] = True
    
    # Build the DP table
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if j < nums[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
    
    return dp[n][target]

#------------------#
# Test Application #
#------------------#

multiset1 = [15, 5, 20, 10, 35, 15, 10]
multiset2 = [15, 5, 20, 10, 35]

print(canPartition(multiset1))  # Expected output: True
print(canPartition(multiset2))  # Expected output: False
