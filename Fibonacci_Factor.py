# This is to solve the Fibonacci Factor puzzle from Amazon on InterviewStreet

def find_smallest_common_factor(K, F):
    """This function finds the smallest common factor
    between an input number K and a Fibonacci number F
    
    Args:
        K: an input number (integer)
        F: a fibonacci number (integer)
    Returns:
        The smallest common factor between K and F
    """
    max_num = max(K, F)
    min_num = min(K, F)
    rem = max_num % min_num
    
    while (rem != 0):
        max_num = min_num
        min_num = rem
        rem = max_num % min_num
    
    return min_num


def compute_output(allK):
    """Compute the output.
    
    Args:
        allK: a list of all input number
    Returns:
        A list of tuple containing the smallest fibonacci number F and
        the smallest common factor between F and an input number K from allK
    """
    ret = []    
    for K in allK:
        curr = 2
        prev = 1
        # gets the current smallest common factor
        scf = find_smallest_common_factor(K, curr)
        while( scf == 1):
            # get the next current fibonacci number
            temp = prev
            prev = curr
            curr = curr + temp
            # compute the smallest common factor with this fibonaccia number
            scf = find_smallest_common_factor(K, curr)
        ret.append((curr, scf))
    return ret
    

def main():
    T = int(raw_input())
    allK = []
    for i in range(T):
        K = int(raw_input())
        allK.append(K)

    output = compute_output(allK)
    for i in output:
        print i[0], i[1]

if __name__ == '__main__':
    main()
