#!/usr/bin/python3
"""
 Find a peak
"""


def find_peak(list_of_integers):
    list= list_of_integers
    if list:
        list.sort()
        return list[-1]
    else:
        return None
