#!/usr/bin/python3
def best_score(a_dictionary):
    """returns the key with the largest integer value from a dictionary."""
    if not a_dictionary:
        return (None)

    return (max(a_dictionary, key = a_dictionary.get))
