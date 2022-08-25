#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    opp = sys.argv[2]
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py {} {} {}".format(a, opp, b))
        exit(1)
    elif opp != '+' and opp != '-' and opp != '*' and opp != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    elif opp == '+':
        print("{} {} {} = {}".format(a, opp, b, add(a, b)))
    elif opp == '-':
        print("{} {} {} = {}".format(a, opp, b, sub(a, b)))
    elif opp == '*':
        print("{} {} {} = {}".format(a, opp, b, mul(a, b)))
    elif opp == '/':
        print("{} {} {} = {}".format(a, opp, b, div(a, b)))
