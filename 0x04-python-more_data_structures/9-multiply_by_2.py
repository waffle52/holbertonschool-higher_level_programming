#!/usr/bin/pthon3
def multiply_by_2(a_dictionary):
    new_list = {}
    for x, y in a_dictionary.items():
        new_list[x] = y * 2
    return (new_list)
