#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a number
    """
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

f = factorial(int(sys.argv[1]))
print(f)
