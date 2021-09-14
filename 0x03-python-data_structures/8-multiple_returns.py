#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]

    if first == 0:
        return(length, None)
    return(length, first)
