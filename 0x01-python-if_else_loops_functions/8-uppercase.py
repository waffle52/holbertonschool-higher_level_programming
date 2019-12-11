#!/usr/bin/python3
def uppercase(str):
    new_text = ""
    for i in str:
        if (ord(i) >= 97 and ord(i) <= 122):
            i = ord(i) - 32
            new_text = new_text + chr(i)
        else:
            new_text = new_text + i
    print("{}".format(new_text), end="")
    print("")
