#!/usr/bin/python3

result = 0


def uniq_add(my_list=[]):
    unique = set(my_list)
    for num in unique:
        result += num


return result
