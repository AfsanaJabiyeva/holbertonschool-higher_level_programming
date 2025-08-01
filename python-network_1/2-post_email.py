#!/usr/bin/python3
"""
Sends a POST request to a given URL with an email as a parameter,
and displays the response body decoded in utf-8.
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data)

    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
