#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value = int
        print("{:d}".format(value))
        return True
    except:
        return False
