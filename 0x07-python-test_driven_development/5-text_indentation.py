#!/usr/bin/python3
def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    it = iter(text)
    for i in it:
        if (i == '.' or i == '?' or i == ':'):
            print("{}".format(i), end="")
            print("\n")
            next(it)
        else:
            print("{}".format(i), end="")
