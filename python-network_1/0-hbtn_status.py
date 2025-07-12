#!/usr/bin/python3
"""
This script fetches https://intranet.hbtn.io/status using urllib
and prints information about the response body.
"""

import urllib.request


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    headers = {"cfclearance": "true"}
    request = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
