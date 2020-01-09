#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    for idx in range(x):
        try:
            print("{}".format(my_list[idx]), end="")
            num += 1
        except:
            break
    print("")
    return (num)
