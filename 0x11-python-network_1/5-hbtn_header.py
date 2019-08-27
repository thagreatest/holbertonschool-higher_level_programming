#!/usr/bin/python3
"""
Sends a request to the URL and displays the value of
the variable X-Request-Id in the response header
"""
import requests
from sys import argv


if __name__ == "__main__":
    res = requests.get(argv[1])
    print(res.headers['X-Request-Id'])
