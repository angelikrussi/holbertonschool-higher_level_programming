#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return None
    for n in range(len(my_list)):
        print("{:}".format(my_list[-n-1]))
