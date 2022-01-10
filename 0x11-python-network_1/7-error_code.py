#!/usr/bin/python3
"""
this script that takes in a URL, sends a request to
the URL and displays the body of the response.
"""
import requests
from sys import argv
if __name__ == '__main__':
    reques = requests.get(argv[1])
    if reques.status_code >= 400:
        print("Error code: {}".format(reques.status_code))
    else:
        print(reques.text)
