#!/usr/bin/python3


def magic_calculation(x, z):
    """Match bytecode provided by Holberton School."""
    from magic_calculation_102 import add, sub

    if x < z:
        c = add(x, z)
        for i in range(4, 6):
            c = add(c, i)
        return (c)

    else:
        return(sub(x, z))
