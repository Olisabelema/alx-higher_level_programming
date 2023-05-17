#!/usr/bin/python3
def subtract_sum_of_less_than_max(list_num):
    max_val = max(list_num)
    to_subtract = sum(filter(lambda x: x < max_val, list_num))
    return max_val - to_subtract
def roman_to_int(roman_string):
    """converts a Roman numeral to an integer."""
    if not type(roman_string) == str:
        return 0
    if not roman_string:
        return 0
    roman_num = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
            }
    list_keys = list(roman_num.keys())
    result = 0
    prev_roman_num = 0
    list_num = [0]

    for index in roman_string:
        for roman_numeral in list_keys:
            if roman_numeral == index:
                if roman_num.get(index)  <= prev_roman_num:
                    result += subtract_sum_of_less_than_max(list_num)
                    list_num = [roman_num.get(index)]
        else:
            list_num.append(roman_num.get(index))
        prev_roman_num = roman_num.get(index)
    result += subtract_sum_of_less_than_max(list_num)    

    return (result)
