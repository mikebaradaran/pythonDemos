#! /bin/python
# Name:        demo_mini_lab.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This program will review the topics covered in
# the QA 2.0 Digital session including objects, string handling,
# file interaction, flow control, simple exception handling.
"""
    Display City weather information.
"""

def c_to_f(temp):
    """ Return temp in Fahrenheit """
    return (float(temp) * 9/5) + 32

def mm_to_inch(height):
    """ Return precipitation in inches """
    return float(height)/25.4


file = input("Enter filename: ")
print("----------------------------------------")
try:
    # Open file handle for Reading in Text mode.
    with open(file, mode="rt") as fh_in:
        # Print header line.
        print(f"{'City':>15s} {'Pop':^10s} {'Rainfall':^8s} {'Temp':^8s}")
        print("-" * 43)

        for line in fh_in:
            (city, pop, temp, rain) = line.split(",") # Split str into list.
            temp_f = c_to_f(temp) # Convert into celsius.
            rain_i = mm_to_inch(rain) # Convert into inches.
            print(f"{city.title():>15s}: {pop:<10s}"
                  f" {temp_f:<5.3f}\N{double prime}"
                  f" {rain_i:>5.2f}\N{degree fahrenheit}")
        # Automatically close file handle.
    print("-" * 43)
except:
    print(f"Error - could not open file {file}")




