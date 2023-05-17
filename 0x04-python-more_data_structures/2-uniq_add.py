#!/usr/bin/python3
def uniq_add(my_list=[]):
    """adds all unique integers in a list (only once for each integer)."""
    integers = filter(lambda x: isinstance(x, int), my_list)
    return sum(set(integers))
