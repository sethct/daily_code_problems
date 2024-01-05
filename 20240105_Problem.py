#| Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#| For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

#-----------------#
# Define function #
#-----------------#
def has_pair(lst, target_sum):
    #| Iterate through each pair of numbers in the list
    for i in range (len(lst)):
           for j in range(i + 1, len(lst)):
                         #| Check if the sume of the current pair equals the target sum
                        if lst[i] + lst[j] == target_sum:
                            #| If found, return the pair of numbers
                            return True, (lst[i], lst[j])
    #| If no pair is found after iterating all pairs, return False
    return False, None

#------------------#
# Test Application #
#------------------#

#| Create example list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#| Give example target
target = 15

#| Call function and receive result in found and pair variables
found, pair = has_pair(numbers, target)

#| Check if pair is found
if found:
       #| If pair is found, print out the component parts and their sum
       print(f'Pair found: {pair[0]} + {pair[1]} = {target}')
#| Execute if no pair is found
else:
       #| Print no pair found
       print('No pair found')

