#| Compute the running median of a sequence of numbers.
#| That is, given a stream of numbers, print out the median of the list so far on each new element.
#| Recall that the median of an even-numbered list is the average of the two middle numbers.

#-----------------#
# Define Function #
#-----------------#

def get_running_median(sequence):
    #| Create list for storage of sorted lists
    sorted_list = []
    #| Create list to store medians
    medians = []
    
    for number in sequence:
        #| Insert the current number into the sorted list, maintaining sorted order
        inserted = False
        for i in range(len(sorted_list)):
            if number < sorted_list[i]:
                sorted_list.insert(i, number)
                inserted = True
                break
        if not inserted:
            sorted_list.append(number)
        
        #| Calculate the median
        n = len(sorted_list)
        if n % 2 == 0:
            #| If even number of elements, average the two middle elements
            median = (sorted_list[n//2 - 1] + sorted_list[n//2]) / 2.0
        else:
            #| If odd, take the middle element
            median = sorted_list[n//2]
        
        #| Append the current median to the list of medians
        medians.append(median)
    
    return medians

#------------------#
# Test Application #
#------------------#

sequence = [2, 1, 5, 7, 2, 0, 5]
medians = get_running_median(sequence)
for median in medians:
    print(median)
