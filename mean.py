#!/usr/bin/env python

def mean(numlist):
    """Calculate the mean of the values in numlist

    Input
    =====
    `numlist` (`list` or `tuple`) - List of values whose mean will be calculated

    Output
    ======
    (`float`) - Mean of the values in numlist
    
    """
    try :
        total = sum(numlist)
        length = len(numlist)
    except TypeError :
        raise TypeError("The list was not numbers.")
    except :
        print "Something unknown happened with the list."
    return total/length