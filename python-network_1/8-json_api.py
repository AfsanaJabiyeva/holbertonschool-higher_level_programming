#!/usr/bin/python3
"""
Takes in a letter, sends a POST request to http://0.0.0.0:5000/search_user
with the letter as parameter 'q', and displays the result based on JSON response.
"""

import requests
import sys

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}

    try:
        response = requests.post(url, data=data)
        response_json = response.json()

        if response_json:
            # Assuming response_json is a dict with 'id' and 'name'
            print(f"[{response_json.get('id')}] {response_json.get('name')}")
        else:
            print("No result")
    except ValueError:
        # .json() raises ValueError if response is not valid JSON
        print("Not a valid JSON")
