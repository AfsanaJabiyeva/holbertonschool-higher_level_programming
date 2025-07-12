#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status and displays its response info.
"""

import urllib.request


def fetch_status():
    """Fetch and display response from https://intranet.hbtn.io/status."""
    url = 'https://intranet.hbtn.io/status'
    req = urllib.request.Request(url)
    req.add_header('cfclearance', 'true')

    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))


if __name__ == "__main__":
    fetch_status()
