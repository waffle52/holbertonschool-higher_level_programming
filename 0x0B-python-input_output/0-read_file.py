#!/usr/bin/python3
def read_file(filename=""):
    """ func to read from a file passed in """
    with open(filename, encoding="utf-8") as MyFile:
        print(MyFile.read(), end="")
