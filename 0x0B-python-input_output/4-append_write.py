#!/usr/bin/python3
def append_write(filename="", text=""):
    """ func to create/append to file """
    with open(filename, "a+", encoding="utf-8") as myFile:
        myFile.write(text)
    return (len(text))
