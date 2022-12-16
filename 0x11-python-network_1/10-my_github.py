#!/usr/bin/python3
"""This script takes GitHub credentials
(username and password) and uses the GitHub API to display your id"""


if __name__ == '__main__':
    import requests
    import sys

    name = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"

    req = requests.get(url, auth=(name, password))
    print(req.json().get('id'))
