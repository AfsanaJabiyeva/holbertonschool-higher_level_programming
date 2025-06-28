#!/usr/bin/python3
"""Module to convert object
to dictionary for JSON serialization."""


def class_to_json(obj):
    """Return the dictionary description of an object."""
    return obj.__dict__
