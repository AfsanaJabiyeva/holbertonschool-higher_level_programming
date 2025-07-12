#!/usr/bin/python3
"""Fetches a URL"""
from urllib import request

if __name__ == "__main__":
    """Makes code executable when it is directly run"""
    url = "https://intranet.hbtn.io/status"
    req = request.Request(url)
    req.add_header('cfclearance', 'true')

    with request.urlopen(req) as response:
        """Opens the url and reads the contents"""
        body = response.read()
        utf8_content = body.decode('utf-8')

    """Prints out the desired output"""
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", utf8_content)

