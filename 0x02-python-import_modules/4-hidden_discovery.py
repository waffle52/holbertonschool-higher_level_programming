#!/usr/bin/python3
if __name__ == "__main__":
    from importlib import import_module
    file = import_module('hidden_4')
    for f in dir(file):
        if f[0] is not '_':
            print("{}".format(f))
