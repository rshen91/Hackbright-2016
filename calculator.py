"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:
    input_string = raw_input("> ")
    tokens = input_string.split(" ") #split returns a list always
    if tokens[0] == "+":
        print add(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == "-":
        print subtract(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == "*":
        print multiply(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == "/":
        print divide(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == "square":
        print square(int(tokens[1]))
    elif tokens[0] == "cube":
        print cube(int(tokens[1]))
    elif tokens[0] == "power":
        print power(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == "mod":
        print mod(int(tokens[1]), int(tokens[2]))
    else:
        break
        

