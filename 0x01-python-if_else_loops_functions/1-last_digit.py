#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
        numbermod = number * -1
        numbermod = number % 10
        numbermod = numbermod * -1
else:
        numbermod = number % 10
        print('Last digit of {:d} is'.format(number), end=" ")
if numbermod == 0:
        print('is {:d} and is 0'.format(numbermod))
elif numbermod < 6:
        print('and is {:d} less than 6 and not 0'.format(numbermod))
elif numbermod > 5:
        print('and is {:d} greater than 5'.format(numbermod))
