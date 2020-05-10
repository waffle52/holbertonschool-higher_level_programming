#!/usr/bin/python3
""" A script that takes in 3 strings
sends a search request to the Twitter API
"""
import requests
import base64
import sys

if __name__ == "__main__":
    consumer_key = sys.argv[1]
    consumer_secret = sys.argv[2]
    search_word = sys.argv[3]

    key_secret = '{}:{}'.format(consumer_key, consumer_secret).encode('ascii')

    b64_encoded_key = base64.b64encode(key_secret)
    b64_encoded_key = b64_encoded_key.decode('ascii')

    url = "https://api.twitter.com/"
    auth_url = '{}oauth2/token'.format(url)

    auth_headers = {
        'Authorization': 'Basic {}'.format(b64_encoded_key),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }

    auth_data = {
        'grant_type': 'client_credentials'
    }

    auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

    access_token = auth_resp.json()['access_token']

    search_headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }

    search_params = {
        'q': search_word,
        'count': 5
    }

    search_url = "{}1.1/search/tweets.json".format(url)
    search_resp = requests.get(search_url, headers=search_headers,
                               params=search_params)
    data = search_resp.json()
    for x in data['statuses']:
        print("[{}] {} by {}".format(x.get('id'), x.get('text'),
                                     x['user']['screen_name']))
