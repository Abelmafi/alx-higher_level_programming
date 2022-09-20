#!/usr/bin/python3
"""deine text_indention function."""


def text_indentation(text):
    """prints a text with 2 lines after each of these characters: ., ? and:.


    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError('text must be string')
    i = 0
    while text[i] == " ":
        i += 1
    while i < len(text):
        print("{}".format(text[i]), end="")
        if text[i] in '.?:' or text[i] == '\n':
            if text[i] in '.?:':
                print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
