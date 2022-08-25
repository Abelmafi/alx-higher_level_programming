#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, div, mul
    a = int(sys.argv[1])
    d = int(sys.argv[3])
    opp = sys.argv[2]
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py {} {} {}".format(a, opp, d))
        sys.exit(1)
    if opp != '+' and opp != '-' and opp != '*' and opp != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    elif opp == '+':
        print("{} {} {} = {}".format(a, opp, d, add(a, d)))
    elif opp == '-':
        print("{} {} {} = {}".format(a, opp, d, sub(a, d)))
    elif opp == '*':
        print("{} {} {} = {}".format(a, opp, d, mul(a, d)))
    elif opp == '/':
        print("{} {} {} = {}".format(a, opp, d, div(a, d)))
