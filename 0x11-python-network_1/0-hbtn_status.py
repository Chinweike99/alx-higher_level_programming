#!/usr/bin/python3
"""Script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

if __name__ == "__main__":
    # Fetching and hndling the resources
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as reply:
        # Reading the content of the response
        content = reply.read()

        #Displaying the body of the response
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
