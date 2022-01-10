#!/usr/bin/python3
"""
this script that takes in a URL and an email address, sends a
POST request to the passed URL with the email as a parameter
"""
import requests
from sys import argv
if __name__ == '__main__':
    reques = requests.post(argv[1], data={'email': argv[2]})
    print(reques.text)
