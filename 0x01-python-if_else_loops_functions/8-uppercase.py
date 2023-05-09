#!/usr/bin/python3
def uppercase(s):
    for c in s:
        if ord('a') <= ord(c) <= ord('z'):
            uppercase_c = chr(ord(c) - 32)
        else:
            uppercase_c = c
        print("{}".format(uppercase_c), end="")
    print()
