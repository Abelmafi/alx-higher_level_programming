#!/usr/bin/python3
"""This script fetches https://alx-intranet.hbtn.io/status"""

if __name__ == '__main__':
    import requests

    url = "https://alx-intranet.hbtn.io/status"
    req = requests.get(url)
    print("Body response:")
    print("\t: {}".format(type(req.text)))
    print("\t: {}".format(req.text))
