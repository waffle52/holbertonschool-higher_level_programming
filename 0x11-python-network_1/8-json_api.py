#!/usr/bin/python3
""" Takes in a letter, sends a POST request with the letter as a parameter """
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if (len(sys.argv) < 2):
        letter = ""
    else:
        letter = sys.argv[1]

    var = {'q': letter}
    r = requests.post(url, data=letter)

    try:
        if r.json().text != {}:
            print("[{}] {}".format(r.json().get('id'), r.json().get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
