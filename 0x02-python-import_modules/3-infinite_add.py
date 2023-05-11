#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Calculate the sum of all arguments
    arguments = sys.argv[1:]  # Get all arguments except the first one (which is the script name)
    total = sum([int(arg) for arg in arguments])

    # Print the total sum
    print("{}".format(total))
