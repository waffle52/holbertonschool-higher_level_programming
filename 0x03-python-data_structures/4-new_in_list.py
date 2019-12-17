#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return (my_list)
    else:
        sec_list = list(my_list)
        sec_list.pop(idx)
        sec_list.insert(idx, element)
        return (sec_list)
