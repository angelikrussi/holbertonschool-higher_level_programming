#!/usr/bin/python3
"""finds a peak """


def find_peak(list_of_integers):
    """funtion finds a peak """
    l = list_of_integers
    if l:
        l.sort()
        return l[-1]
    else:
        return None
