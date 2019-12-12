#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        n = len(str) - n
    strn = str[:n] + str[n+1:]
    return (strn)
