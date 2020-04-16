#!/usr/bin/python3
""" Sends a POST request and displays response """
import requests
import sys

if __name__ == "__main__":
    payload = {'email': sys.argv[2]}
    url = sys.argv[1]
    r = requests.post(url, data=payload)
    print(r.text)
