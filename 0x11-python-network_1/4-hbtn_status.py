#!/usr/bin/python3
"""displays the value of the X-Request-Id variable found in
the header of the response.
"""
import requests

if __name__ == "__main__":

    reply = get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print("\t- type: {}".format(reply.text.__class__))
    print("\t- content: {}".format(reply.text))
