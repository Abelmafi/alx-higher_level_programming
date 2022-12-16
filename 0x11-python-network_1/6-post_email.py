#!/usr/bin/python3
"""This script that takes in a URL and an email address, sends
a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response."""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    req = requests.post(url, data=data)
    print(req.text)
