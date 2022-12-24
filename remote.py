#!/usr/bin/env python

"""
This allows easily creating req-resp interactions
"""

import requests

TARGET = "http://localhost/"
METHOD = "GET"

def get_auth():
    """
    This should be (user, pass)
    """
    return None

def get_headers():
    """
    This can be used to set content-types and etc...
    """
    return []

def get_proxies():
    """
    This can be used to enable Burp so some debug can be done

    Format: {'http': 'http://localhost:8080'}
    """
    return None

def input_decorator(data):
    """
    This should transform/decorate the data as needed
    """
    return data

def parse_req(req):
    """
    Parse the request output as needed.
    """
    return ""

def main():
    """
    This is the actual code that works.
    """
    while True:
        inp = input('> ').strip()

        # Easily exit the script
        if inp in ('quit', 'q', 'Q'):
            return

        req = requests.request(METHOD,
                               TARGET,
                               data=input_decorator(inp),
                               auth=get_auth(),
                               headers=get_headers(),
                               timeout=(1, 3),
                               proxies=get_proxies()
                               )

        print(parse_req(req))


if __name__ == "__main__":
    main()
