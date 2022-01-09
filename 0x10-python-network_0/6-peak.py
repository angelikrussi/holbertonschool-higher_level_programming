#!/usr/bin/python3
"""finds a peak """


def find_peak(list_of_integers):
    """funtion finds a peak """
    list = list_of_integers
    if list:
        list.sort()
        return list[-1]
    else:
        return None
