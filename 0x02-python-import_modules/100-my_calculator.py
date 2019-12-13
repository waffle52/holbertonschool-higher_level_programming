#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1

    if (len(sys.argv) - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    word = sys.argv[2]
    b = int(sys.argv[3])
    result = 0
    if word is '+':
        result = calculator_1.add(a, b)
    elif word is '-':
        result = calculator_1.sub(a, b)
    elif word is '*':
        result = calculator_1.mul(a, b)
    elif word is '*':
        result = calculator_1.div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, word, b, result))
