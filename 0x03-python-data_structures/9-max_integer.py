#!/usr/bin/python3

def max_integer(my_list=[]):
    """ finds the biggest integer of a list."""
    if not my_list:
        return None
    maximum_number = my_list[0]
    for index in my_list:
        if index > maximum_number:
            maximum_number = index
    return (maximum_number)
