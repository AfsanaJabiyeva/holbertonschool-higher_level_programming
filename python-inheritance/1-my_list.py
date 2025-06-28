#!/usr/bin/python3
"""
Module that defines a class MyList that inherits from list.
"""


class MyList(list):
    """
    A subclass of the built-in
    list class with a method to print the list sorted.
    """
    def print_sorted(self):
        """
        Prints the list in ascending sorted order
        """
        print(sorted(self))
