#!/usr/bin/python3
"""
Function that returns the list of
available attributes and methods of an objec
"""


def lookup(obj):
    """list of available attributes"""
    return dir(obj)
