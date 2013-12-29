# This is to solve Meeting Schedules from Amazon on Interview Street
# follow this link https://amazon.interviewstreet.com/challenges/dashboard/#problems

# convert HH/MM into an array of only minutes: 60*24 length
# when reading the input, convert HH and MM to corrensponding positions
# in the array and mark them as False
# conversion formula: 
# HH MM -> number
# int(HH) * 60 + int(MM)
# eg: 00 30 -> 0*60 + 30 = 30
#     02 15 -> 2*60 + 15 = 135
#     23 59 -> 23*60 + 59 = 1439
# 
# number -> HH MM
# HH = number/60
# MM = number%60


def init_mins_arr():
    """Initialize a minutes array of length 60*24.
    Args:
        None
    Return:
        A boolean array of length 60*24.
        True by default, meaning not busy
    """
    mins = []
    size = 60*24
    for i in range(size):
        mins.append(True)
    return mins


def convert_to_mins(hh, mm):
    """Convert HH MM format to only MM format
    
    Args:
        hh: hour
        mm: minute
    Returns:
        a number indicates the minutes equivalent to hh mm format
    """
    return 60*hh + mm


def convert_to_hhmm(mins):
    """Convert MM format HH MM format.
    
    Args:
        mins: the minutes equivalence of HH MM
    Returns:
        hh mm in string 
    """
    if (mins == 60*24):
        return ('00', '00')
    hh = mins/60
    mm = mins%60
    if hh<10:
        hh = '0%s' % str(hh)
    else:
        hh = str(hh)
    if mm<10:
        mm = '0%s' % str(mm)
    else:
        mm = str(mm)
    return hh, mm
        

def mark_busy_times(mins_arr, start_mins, end_mins):
    """Mark busy times in the minutes array by setting the boolean value to False.
    
    Args:
        mins_arr: the minute array
        start_mins: start time
        end_mins: end time
    """
    for i in range(start_mins, end_mins):
        mins_arr[i] = False
    
    
def get_busy_time(mins_arr, input):
    """Converting busy time slots from HH MM format to boolean values in mins_arr.
    
    Args:
        mins_arr: a minutes array of length 24*60
        input: input array with format StartHH StartMM EndHH EndMM
    Returns:
        None
    """
    
    StartHH = int(input[0])
    StartMM = int(input[1])
    EndHH = int(input[2])
    EndMM = int(input[3])
    
    start_mins = convert_to_mins(StartHH, StartMM)
    end_mins = convert_to_mins(EndHH, EndMM)
    
    mark_busy_times(mins_arr, start_mins, end_mins)


def get_available_time(mins_arr):
    """Get all not busy time slots.
    
    Args:
        minnutes array
    Returns:
        an array of tuple of available time slots (start_mins, end_mins)
    """
    avail_slots = []
    curr = 0
    while (curr < len(mins_arr)):
        # start busy time slots
        if mins_arr[curr] == False:
            while(curr < len(mins_arr) and mins_arr[curr] == False):
                curr += 1
        start = curr

        # end busy time slots
        if mins_arr[curr] == True:
            while(curr < len(mins_arr) and mins_arr[curr] == True):
                curr += 1
        if curr >= len(mins_arr):
            end = len(mins_arr)
        else:
            end = curr

        # add start and end times to avail_slots
        avail_slots.append((start, end))
        curr += 1
    
    return avail_slots
    

def pick_slots(avail_slots, K):
    """Pick all slots that satisfy duration requirements.
    
    Args:
        avail_slots: an array of all available time slots
        K: the time duration requirement
    Returns:
        A list of time slots that meet requirements.
    """
    corr_slots = []
    for slot in avail_slots:
        if slot[1] - slot[0] >= K:
            corr_slots.append(slot)
    return corr_slots


def print_slots(slots):
    """Print slots in a formatted way.
    
    Args:
        a list of time slots
    Returns:
        None
    """
    for slot in slots:
        start_time = convert_to_hhmm(slot[0])
        end_time = convert_to_hhmm(slot[1])
        print start_time[0], start_time[1], end_time[0], end_time[1]


def main():
    mins_arr = init_mins_arr()

    line = raw_input().split(' ')
    M = int(line[0])
    K = int(line[1])
    for i in range(M):
        line = raw_input().split(' ')
        get_busy_time(mins_arr, line)    
    avail_slots = get_available_time(mins_arr)
    print_slots(pick_slots(avail_slots, K))


main()