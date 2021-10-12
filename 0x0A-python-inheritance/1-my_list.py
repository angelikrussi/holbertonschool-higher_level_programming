#!/usr/bin/python3
"""Contains the MyList class"""


class MyList (list):

    """MyList class that inherits from the list class"""

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
