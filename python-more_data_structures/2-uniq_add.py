#!/usr/bin/python3

def uniq_add(my_list=[]):
    return sum(set(my_list))


if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print(f"Result: {result}")
