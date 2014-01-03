# This is to solve the Lyft Programming Challenge
import math

def distance_between(p1, p2):
    """This calculates the linear distance between two points
    on a 2D coordinates system.
    
    Args:
        p1: the start point (a tuple of x,y coordinates)
        p2: the end point (a tuple of x,y coordinates)
    Returns:
        the linear distance between the 2 points
    """
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


def find_shorter_detour(pA, pB, pC, pD):
    """Find shorter detour route between two pair of start and end points.
    
    Args:
        pA: start point A for the first person (a tuple of x,y coordinates)
        pB: end point B for the first person (a tuple of x,y coordinates)
        pC: start point C for the second person (a tuple of x,y coordinates)
        pD: end point D for the second person (a tuple of x,y coordinates)
    Returns:
        the shorter detour distance between these two pairs
        either detour (A->C->D->B) or detour (C->A->B->D)
        and the detour direction
    """
    
    # Observation: (A->C->D->B) - (C->A->B->D) is actually
    # equivalent to [(C->D) - (A->B)] 
    # Hence, if the distance between C and D is greater than the distance
    # between A and B, then the detour through CD is more efficient than
    # the detour through AB
    # This makes sense because the detour through CD crosses AB length, which
    # is shorter than CD length in the detour through AB
    
    detour_diff = distance_between(pC, pD) - distance_between(pA, pB)
    if detour_diff >= 0:
        route = 'C->A->B->D'
    else:
        route = 'A->C->D->B'
    
    return abs(detour_diff), route