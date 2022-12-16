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
    req = request.post(url, data=data)
    try:
        __dict = req.json()
        if __dict == {}:
            print("No result")
        else:
            print("[{}] {}".format(__dict.get('id'), __dict.get('name')))
    except ValueError:
        print("Not a valid JSON")
