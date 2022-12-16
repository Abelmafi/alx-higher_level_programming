#!/usr/bin/python3
"""This script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter."""


def get_url(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.raw


if __name__ == '__main__':
    import requests
    from sys import argv

    url = argv[1]
    try:
        req = get_url(url)
        print(req)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.response.status_code))
