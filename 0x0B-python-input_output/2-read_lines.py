#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """ func to print file as whole or by line limit """
    with open(filename, encoding="utf-8") as MyFile:
        if nb_lines <= 0 or nb_lines >= len(MyFile.readlines()):
            print(MyFile.read(), end="")
        else:
            MyFile.seek(0)
            for i in range(1, nb_lines + 1):
                print(MyFile.readline(), end="")
