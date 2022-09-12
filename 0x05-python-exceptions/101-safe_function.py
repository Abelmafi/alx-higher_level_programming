#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as exc:
        print("Excption:", exc, file=sys.stderr)
        return (None)
    else:
        return res
