#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

url = "https://alx-intranet.hbtn.io/status"

if __name__ == "__main__":

    with urllib.request.urlopen(url) as response:
        html = response.read()
        utf = html.decode('utf-8')
    print("Body response:")
    print("\t- type:", type(html))
    print("\t- content:", html)
    print("\t- utf-8 content:", utf)
