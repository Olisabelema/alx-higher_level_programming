#!/usr/bin/python3
def weight_average(my_list=[]):
    """returns the weighted average of all integers tuple (<score>, <weight>)."""
    if not my_list:
        return 0

    weighted_sum = sum(score * weight for score, weight in my_list)
    sum_weights = sum(weight for _, weight in my_list)

    return weighted_sum / sum_weights
