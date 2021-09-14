#!/usr/bin/python3
def max_integer(my_list=[]):

    if len(my_list) == 0:
        return None
    max_value = 0
    for num in my_list:
        if (max_value is None or num > max_value):
            max_value = num
    return max_value
