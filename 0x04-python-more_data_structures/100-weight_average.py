#!/usr/bin/python3

def weight_average(my_list=[]):
    """returns the weighted average of all integers tuple."""
    if not my_list:
        return 0

    weighted_sum = 0
    sum_weights = 0

    for t in my_list:
        weighted_sum += t[0] * t[1]
        sum_weights += t[1]

    return (weighted_sum/sum_weights)
