#!/usr/bin/python3
if __name__ == "__main__":
    import sys
i = len(sys.argv) - 1
word = "arguments:"
if i == 0:
    word = "arguments."
if i == 1:
    word = "argument:"
print("{} {}".format(i, word))
for x in range(1, i + 1):
    print("{}: {}".format(x, sys.argv[x]))
