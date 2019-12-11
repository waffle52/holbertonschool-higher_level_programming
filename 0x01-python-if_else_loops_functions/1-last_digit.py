#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = int(str(number)[-1:])
print("Last digit of {} is {} and is ".format(number, digit), end = "")
if digit > 5:
    print("greater than 5")
elif digit == 0:
    print("0")
elif digit < 6 and digit != 0:
    print("less than 6 and not 0")
