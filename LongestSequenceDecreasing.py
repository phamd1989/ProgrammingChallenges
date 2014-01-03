# this is to solve the Longest Increasing Subsequence problem 
# the idea is to record all possible solutions up to this element of the orginial list
# recursive function: L[i+1] = best_solution[i].append(this element at i+1)

from operator import itemgetter


def longest_sequence_decreasing(input_arr, solutions, curr):
    """This function is to find all possible decreasing subsequence from the original array.
    
    Args:
        input_arr: the original input array, assuming a list of tuple(gpa, sat)
        solutions: all possible decreasing subsequences from the input array
        curr: the current element from the input_arr
    Returns:
        None
    """
    # don't go over the maximum length
    if curr >= len(input_arr):
        return
    
    curr_element = input_arr[curr]
    # construct the best solution up to this current element
    best_solution = curr_longest_sequence(solutions, curr_element)
    # add the best_solution at this element to solutions
    solutions.append(best_solution)
    # recursivelly compute all other solutions
    curr += 1
    longest_sequence_decreasing(input_arr, solutions, curr)


def curr_longest_sequence(solutions, curr_element):
    """Add curr_element to the longest decreasing sequence found in the solutions array.
    If no sequence found, intialize an empty list and adds curr_element to it.
    
    Args:
        solutions:  current solutions array of all decreasing sequences
        curr_element: current element of the original array
    Returns:
        a list of the longest decreasing sequence up to curr_element
    """
    best_solution = []
    for solution in solutions:
        # check if curr_element[0] - the gpa part, is less than all elements in solution
        # and solution has more items than best_solution
        if solution[-1][0] > curr_element[0] and len(solution) > len(best_solution):
            best_solution = solution[:]
    # append curr_element to the end of best_solution
    best_solution.append(curr_element)
    return best_solution


def print_longest_decreasing_sequence(solutions):
    """Pick the longest decreasing sequence from all possible decreasing sequences.
    
    Args:
        solutions:  all possible decreasing sequences
    Returns:
        the longest item in the solutions array
    """
    best_solution = []
    for solution in solutions:
        if len(solution) > len(best_solution):
            best_solution = solution
    return best_solution


def sort_input_array_by_gpa(input_arr):
    """Sort the input array in the ascending order of gpa
    
    Args:
        input_arr: the original input array
    Returns:
        the gpa-sorted version of the original input array
    """
    return sorted(input_arr, key=itemgetter(1))


def test():
    
    # test case 1
    data = [(2.8, 620), (3.5, 610), (3, 613), (3.7, 587), (3.6, 570),
            (2.9, 607), (3.2, 650), (2.7, 597), (2.5, 727), (3.4, 577),
            (3.1, 693)]
    data = sort_input_array_by_gpa(data)
    solutions = []
    longest_sequence_decreasing(data, solutions, 0)
    actual_output = print_longest_decreasing_sequence(solutions)
    expected_output = [(3.6, 570), (3.4, 577), (2.9, 607), (2.8, 620), (2.5, 727)]
    assert (actual_output == expected_output)
    
    # test case 2
    data = [(2.0, 620), (3.5, 610), (3, 613), (2.7, 587), (3.6, 570)]
    data = sort_input_array_by_gpa(data)
    solutions = []
    longest_sequence_decreasing(data, solutions, 0)
    actual_output = print_longest_decreasing_sequence(solutions)
    expected_output = [(3.6, 570), (3.5, 610), (3, 613), (2.0, 620)]
    assert (actual_output == expected_output)
    
    # test case 3
    data = [(1, 620), (2, 610), (3, 603), (4, 587)]
    data = sort_input_array_by_gpa(data)
    solutions = []
    longest_sequence_decreasing(data, solutions, 0)
    actual_output = print_longest_decreasing_sequence(solutions)
    expected_output = [(4, 587), (3, 603), (2, 610), (1, 620)]
    assert (actual_output == expected_output)
    
    # test case 4
    data = [(1, 620), (2, 670), (3, 703)]
    data = sort_input_array_by_gpa(data)
    solutions = []
    longest_sequence_decreasing(data, solutions, 0)
    actual_output = print_longest_decreasing_sequence(solutions)
    expected_output = [(1, 620)]
    assert (actual_output == expected_output)
    
    
test()