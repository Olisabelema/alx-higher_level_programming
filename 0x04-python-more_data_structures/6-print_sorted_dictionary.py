#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """prints a dictionary by ordered keys."""
    order_list = list(a_dictionary.keys())
    order_list.sort()
    for index in order_list:
        print("{}: {}".format(index, a_dictionary.get(index)))
