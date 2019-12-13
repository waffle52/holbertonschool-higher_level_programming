#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    word = sys.argv[2]
    b = int(sys.argv[3])
    result = 0
    if word is '+':
        result = add(a, b)
    elif word is '-':
        result = sub(a, b)
    elif word is '*':
        result = mul(a, b)
    elif word is '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, word, b, result))
