#!/usr/bin/python3

def no_c(my_string):
    output = ""
    for c in my_string:
        if c != "c" and c != "C":
            output += my_string
    return output
