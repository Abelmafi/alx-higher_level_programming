#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, div, mul
    a = int(sys.argv[1])
    d = int(sys.argv[3])
    opp = {"+": add, "-": sub, "*": mul, "/": div}
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if sys.argv[2] not in list(opp.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    d = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], d, opp[sys.argv[2]](a, d)))
