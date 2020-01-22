#!/usr/bin/python3
def number_of_lines(filename=""):
    """ func to get number of lines in passed file """
    with open(filename, encoding="utf=8") as MyFile:
        for i, l in enumerate(MyFile):
            pass
        return (i + 1)
