#!/usr/bin/python3
"""displays the value of the X-Request-Id variable found in
the header of the response.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    reply = requests.post(url, data=value)
    print(reply.text)
