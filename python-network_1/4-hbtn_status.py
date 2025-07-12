#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using requests
and displays the response body.
"""

import requests

if __name__ == "__main__":
    response = requests.get("https://intranet.hbtn.io/status")
    content = response.text
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
