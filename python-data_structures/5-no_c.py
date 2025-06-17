#!/usr/bin/python3

def no_c(my_string):
    output = ""
    for i in my_string:
        if i != "c" and i != "C":
            output += i
    return output
