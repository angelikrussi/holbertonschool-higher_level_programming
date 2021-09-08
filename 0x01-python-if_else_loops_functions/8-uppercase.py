#!/usr/bin/python3
def uppercase(str):
    for may in str:
        may = ord(str)
        if may >= 97 and may <= 122:
            may -= 32
        may = chr(may)
        print("{:c}".format(may), end='')
    print(" ")