#!/usr/bin/python3
"""script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter."""

if __name__ == '__main__':
    import requests
    from sys import argv

    url = "http://0.0.0.0:5000/search_user"
    if len(argv) > 1:
        id_value = argv[1]
    else:
        id_value = ""
    data = {'q': id_value}
    req = requests.post(url, data=data)
    try:
        _dict = req.json()
        if _dict == {}:
            print("No result")
        else:
            print("[{}] {}".format(_dict.get('id'), _dict.get('name')))
    except ValueError:
        print("Not a valid JSON")
