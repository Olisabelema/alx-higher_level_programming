#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """returns a new dictionary with all values multiplied by 2."""
    new_dict = a_dictionary.copy()
    key_list = list(new_dict.keys())

    for index in key_list:
        new_dict[index] = new_dict[index] * 2

    return (new_dict)
