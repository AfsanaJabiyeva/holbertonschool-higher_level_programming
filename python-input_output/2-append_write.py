#!/usr/bin/python3
"""comment"""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file (UTF8)
    returns the number of characters added"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
