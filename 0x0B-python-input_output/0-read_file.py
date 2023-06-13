#!/usr/bin/python3
"""
0-read_file.py
a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """read file utf8 con with """
    with open(filename, encoding='UTF-8') as file:
        for line in file:
            print(line, end='')

