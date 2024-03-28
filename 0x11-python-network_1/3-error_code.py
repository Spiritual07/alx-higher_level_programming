#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8)
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        urllib.request.urlopen(request)
    except urllib.error.HTTPError as e:
        print(e.code)
