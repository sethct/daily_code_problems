#| The power set of a set is the set of all its subsets.
#| Write a function that, given a set, generates its power set.
#| For example, given the set {1, 2, 3}, it should return
#| {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
#| You may also use a list or array to represent a set.

#-----------------#
# Define Function #
#-----------------#

def power_set(s):
    #| Base case: the power set of an empty set is a set containing the empty set.
    if len(s) == 0:
        return [[]]
    
    #| Recursive case: take an element out and generate the power set for the rest.
    #| Then, add the taken element to each subset of the power set of the rest.
    else:
        rest_power_set = power_set(s[:-1])
        current_element = s[-1]
        #| For each subset in the power set of the rest, create a new subset
        #| that includes the current element.
        with_current = [subset + [current_element] for subset in rest_power_set]
        #| The complete power set includes subsets with and without the current element.
        return rest_power_set + with_current

#------------------#
# Test Application #
#------------------#

s = [1, 2, 3]
print(power_set(s))