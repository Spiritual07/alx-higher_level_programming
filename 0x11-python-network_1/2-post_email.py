#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of
the response (decoded in utf-8)
"""

import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]
    parse_data = urllib.parse.urlencode({"email": email})
    data = parse_data.encode("ascii")
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        body = response.read().decode('utf-8')
    print(body)
