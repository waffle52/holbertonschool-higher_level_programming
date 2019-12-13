#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv) - 1
    char = ':'
    if i == 0:
        char = '.'
    print("{} arguments{}".format(i, char))
    for x in range(1, i + 1):
        print("{}: {}".format(x, sys.argv[x]))
