#!/usr/bin/python3
"""displays the value of the X-Request-Id variable found in
the header of the response.
"""
import urllib.error
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)

    # Using the try statement to ensure proper handling
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as d:
        print("Error code: {}".format(d.code))
