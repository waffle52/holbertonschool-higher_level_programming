#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return (None)
    else:
        biggest = 0
        length = len(my_list) - 1
        for i in range(length):
            if biggest < my_list[i]:
                biggest = my_list[i]
        return (biggest)
