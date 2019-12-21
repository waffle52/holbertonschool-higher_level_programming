#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    cur_list = set(set_1).union(set(set_2))
    for x in set_1:
        for y in set_2:
            if x == y:
                cur_list.remove(x)

    return (cur_list)
