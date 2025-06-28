#!/usr/bin/python3
"""
Function that returns True if the object is exactly
An instance of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """Function"""
    return type(obj) == a_class
