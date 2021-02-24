#!/usr/bin/env python

# Simple CLI calculator
# example usage: ./calc.py 10 + 2
#         output: 12

# This allows us to use python3 style print statements when running as python2
# good for future compatibility
from __future__ import print_function

# This makes all division done with floats by default
# without this, python2 would evaluate '3 / 2' as '1'
from __future__ import division

# module level imports here
import sys


# Add operand1 to operand2
def addition(operand1, operand2):
    return operand1 + operand2


# Subtract operand2 from operand1
def minus(operand1, operand2):
    return operand1 - operand2


# this will run if calc.py is ran from the terminal
if __name__ == "__main__":

    # try and parse the user input
    try:
        operand1 = float(sys.argv[1])
        operator = sys.argv[2]
        operand2 = float(sys.argv[3])
    except ValueError:
        # something went wrong trying to parse the user input
        # Inform the user how to use
        print("Usage: ./calc.py 10 + 2")

        # return with error status 1
        # since something went wrong
        sys.exit(1)

    # get result of mathematical operation
    result = None
    if operator == '+':
        result = add(operand1, operand2)
    elif operator == '-':
        result = minus(operand1, operand2)

    # see if we got an answer
    if result is None:
        # no result, probably an unsupported operator
        print("operator \"" + operator + "\" not supported")
    else:
        # we got an answer!
        # give it to the user
        print(str(result))
