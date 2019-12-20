#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    num = 0
    name = ""
    for x, y in a_dictionary.items():
        if y > num:
            num = y
            name = x
    return (name)
