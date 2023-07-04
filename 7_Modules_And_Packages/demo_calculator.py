#! /usr/bin/python
# Author: QA2.0 LIVE, V1.0
# Description: This program will 
"""
    Docstring: This program/module will..
"""

#! /usr/bin/python
# Author: DCameron, V1.0, email
# Description: This program will demonstrate another example of
# creating functions with DocStrings, parameter passing, return values.
"""
    Calculator program with Add, Divide and Multiply functionality.
"""
import sys
import unittest

def multiply(x, z):
    """  Accepts two numeric parameters and return product.  """
    return x * z

def add(x, z):
    """   Accepts two numeric parameters, adds them and returns sum. """
    return x + z

def divide(x, z):
    """ Accepts two numeric parameters, divides first by the second and returns result.    """
    return f"{x/z:.3f}"

def test_add():
    unittest.assertEqual(8, add(4, 3))
    return None

def test_multiply():
    unittest.assertEqual(12, multiply(4, 3))
    return None

def test_divide():
    unittest.assertEqual('1.333', divide(4, 3))
    return None


def main():
    """ Single Line docstrings are ideal if the function is self explanatory """
    print(f"4 * 3 = {multiply(4, 3)}")
    print(f"4 + 3 = {add(4, 3)}")
    print(f"4 / 3 = {divide(4, 3)}")

    return None

if __name__ == "__main__":
    unittest.main()
    main()
    sys.exit(0)

