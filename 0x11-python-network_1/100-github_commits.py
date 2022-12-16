#!/usr/bin/python3
"""This script list 10 commits (from the most recent to oldest) of
the repository “rails” by the user “rails”"""


if __name__ == '__main__':
    import requests
    import sys

    respo = sys.argv[1]
    user = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(respo, user)
    req = requests.get(url)
    count = 0
    for i in req.json():
        print("{}: {}".format(i.get('sha'), i.get('commit').get('author').get('name')))
        count += 1
        if count == 10:
            break
