#!/usr/bin/python3
""" Script that takes url as argument than sends a request """
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.read()
        print("{}".format(response.headers['X-Request-Id']))
