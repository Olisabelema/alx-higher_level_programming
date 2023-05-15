#!/bin/usr/python3

def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order."""
    reversed_list = my_list[::-1]
    for i in reversed_list:
        print("{:d}".format(i))
