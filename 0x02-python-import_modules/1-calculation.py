#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of 10 and 5."""
    from calculator_1 import add, sub, mul, div

    x = 10
    z = 5

    print("{} + {} = {}".format(x, z, add(x, z)))
    print("{} - {} = {}".format(x, z, sub(x, z)))
    print("{} * {} = {}".format(x, z, mul(x, z)))
    print("{} / {} = {}".format(x, z, div(x, z)))

