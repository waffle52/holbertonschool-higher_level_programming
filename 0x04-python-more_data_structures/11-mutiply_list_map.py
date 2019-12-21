#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    cur_list = map(lambda x: x * number, my_list)
    return (list(cur_list))
