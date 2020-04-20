#!/usr/bin/python3
""" Script to print 10 recent commits with sha and author name """
import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    r = requests.get(url)
    y = 10
    data = r.json()
    if (len(data) < y):
        y = len(data)
    for x in range(0, y):
        print("{}: {}".format(data[x]['sha'],
                              data[x]['commit']['author']['name']))
