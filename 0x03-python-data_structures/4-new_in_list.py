#!/bin/usr/python3

def new_in_list(my_list, idx, element):
    """Return a new list with an element replaced at a specific position."""
    if idx < 0 or idx >= len(my_list):
        return (my_list.copy())

    new_list = my_list.copy()
    new_list[idx] = element
    return (new_list)
