#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        index = 0
        while count < x:
            if isinstance(my_list[index], int):
                print("{:d}".format(my_list[index]), end="")
                count += 1
                if count == x:
                    break
            index += 1
        print()
        return (count)
    except IndexError:
        raise
