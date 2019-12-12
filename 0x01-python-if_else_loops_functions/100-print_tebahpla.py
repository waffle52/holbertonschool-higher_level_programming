#!/usr/bin/python3
take = 0
for i in range(122, 96, -1):
    if (i % 2) == 1:
        take = 32
    print("{}".format(chr(i - take)), end="")
    take = 0
