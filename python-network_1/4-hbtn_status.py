#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using requests
with cfclearance header to bypass Cloudflare protection.
"""

import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    headers = {'cfclearance': 'true'}
    response = requests.get(url, headers=headers)
    content = response.text
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
