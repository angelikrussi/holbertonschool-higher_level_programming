#!/usr/bin/python3
""" Find a peak."""


def find_peak(list_of_integers):
    """funtion finds  peak """
    lis = list_of_integers
    if lis:
        lis.sort()
        return lis[-1]
    else:
        return None
