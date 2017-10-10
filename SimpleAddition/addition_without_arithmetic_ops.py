
""" 
This code does the addition of 2 integers
without using any arithmetic operations.
"""

import sys

"""
This function does a bitwise sum of 2 integers.
XOR operation represents the sum of 2 bits.
AND operation obtains the carry bit.
"""
def Add(x, y):
    print(x, y)
    return x if y == 0 else Add(x ^ y, (x & y) << 1)

if __name__ == '__main__':
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    res = Add(x, y)

    print('{} + {} = {}'.format(x, y, res))
