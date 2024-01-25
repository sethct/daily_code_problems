#| Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
#| find the minimum number of rooms required.
#| For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.


#-----------------#
# Define Function #
#-----------------#

def min_rooms(intervals):
    #| If there are no intervals, no rooms are needed
    if not intervals:
        return 0

    #| Extract start times and end times from the intervals and sort them
    start_times = sorted([interval[0] for interval in intervals])
    end_times = sorted([interval[1] for interval in intervals])

    #| Initialise pointers for start and end times
    start_ptr, end_ptr = 0, 0

    #| Initialise counters for maximum rooms needed and current rooms in use
    max_rooms, current_rooms = 0, 0

    #| Loop through all the intervals
    while start_ptr < len(intervals):
        #| If the next start time is earlier or equal to the next end time
        if start_times[start_ptr] < end_times[end_ptr]:
            #| It means a new lecture is starting, so increment the room count
            current_rooms += 1
            start_ptr += 1  # Move to the next start time

            #| Update the maximum number of rooms needed so far
            max_rooms = max(max_rooms, current_rooms)
        else:
            #| If the next end time is earlier, it means a lecture has finished
            current_rooms -= 1
            end_ptr += 1  # Move to the next end time

    #| Return the maximum number of rooms needed at any point in time
    return max_rooms

#------------------#
# Test Application #
#------------------#

intervals = [(30, 75), (0, 50), (60, 150)]
print(min_rooms(intervals))  # Output should be 2
