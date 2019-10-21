#!/usr/bin/python
# Arithmetic Parser for Plexsys by Angela Ong
# Be sure to use Python3+

from parser import Parser

while True:
    raw_expression = input("Enter expression to be evaluated: ")
    if raw_expression == "exit":
        break
    parser = Parser(raw_expression)
    result = parser.parse()
    print(result.evaluate())
