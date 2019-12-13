#!/usr/bin/python3
if __name__ == "__main__":
    from importlib import import_module
    ModuleType = import_module('calculator_1')

a = 10
b = 5
print("{} + {} = {}".format(a, b, ModuleType.add(a, b)))
print("{} - {} = {}".format(a, b, ModuleType.sub(a, b)))
print("{} * {} = {}".format(a, b, ModuleType.mul(a, b)))
print("{} / {} = {}".format(a, b, ModuleType.div(a, b)))
