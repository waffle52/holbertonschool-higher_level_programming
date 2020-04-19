#!/usr/bin/python3
""" Script takes GitHub credentials to display github id """
import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    url = "https://api.github.com/user"
    set = {sys.argv[1]: sys.argv[2]}
    try:
        r = requests.get(url, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
        data = r.json()
        data = dict(data)
        print("{}".format(data['id']))
    except:
        print("None")
