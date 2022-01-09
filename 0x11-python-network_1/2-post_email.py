#!/usr/bin/python3
""" script that takes in a URLemail, sends a POST request to the passed URL"""
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')

    with urllib.request.urlopen(url, data) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))
