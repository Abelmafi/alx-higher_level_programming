#!/usr/bin/python3
"""This script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter."""

if __name__ == '__main__':
    import requests
    from sys import argv

    url = argv[1]
    try:
        req = requests.get(url)
        req.raise_for_status()
        print(req.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.status_code))
