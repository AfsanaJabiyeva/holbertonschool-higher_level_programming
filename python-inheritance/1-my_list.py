#!/usr/bin/python3
"""
Module that defines a class MyList that inherits from list.
"""
class MyList(list):
    def print_sorted(self):
        """
        Prints the list in ascending sorted order (does not modify original list).
        """
        print(sorted(self))
