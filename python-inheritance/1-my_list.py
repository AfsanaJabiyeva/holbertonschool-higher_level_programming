#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """A subclass of list that provides additional functionality."""

    def print_sorted(self):
        """Print the list in ascending sorted order 
        The method prints a new list sorted in ascending order.
        Works with all integer values including negative numbers.
        Does not modify the original list.
        """
        print(sorted(self))
