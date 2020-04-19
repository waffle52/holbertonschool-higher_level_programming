#!/usr/bin/python3
""" Script to """
import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[1], sys.argv[2])
    r = requests.get(url)
    data = r.json()
    for x in range(0, 10):
        print("{}: {}".format(data[x]['sha'],
                              data[x]['commit']['author']['name']))
