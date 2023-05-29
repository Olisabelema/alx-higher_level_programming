#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for index in list_keys:
        if value == a_dictionary.get(index):
            del a_dictionary[index]

    return (a_dictionary)
