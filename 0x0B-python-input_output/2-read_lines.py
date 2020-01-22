#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """ func to print file as whole or by line limit """
    with open(filename, encoding="utf-8") as MyFile:
        if nb_lines <= 0 or nb_lines >= len(MyFile.readlines()):
            print(MyFile.read())
        else:
            with open(filename, encoding="utf-8") as MyFileTest:
                for i in range(0, nb_lines):
                    print(MyFileTest.readline(), end="")
