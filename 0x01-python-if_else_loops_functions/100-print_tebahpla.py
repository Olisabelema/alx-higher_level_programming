#!/usr/bin/python3

""""Print the alphabet in reverse order alternating upper- and lower-case."""
i = 0
for i in range(90, 64, -1):
    print("{:c}".format(i + 32) if i % 2 == 0 else "{:c}".format(i), end="")
