#!/usr/bin/python3
""" Takes in a letter, sends a POST request with the letter as a parameter """
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if (len(sys.argv) >= 2):
        letter = {'q': sys.argv[1]}
    else:
        letter = {'q': ''}
    r = requests.post(url, letter)
    try:
        if (r.json() and r.json != ""):
            print("[{}]: {}".format(r.json().get('id'), r.json().get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
