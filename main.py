#!/usr/bin/python
# Arithmetic Parser for Plexsys by Angela Ong
# Be sure to use Python3+

from parser import get_sum, evaluate_tree

while True:
    # Get expression
    raw_expression = input("Enter expression to be evaluated: ")
    if raw_expression == "exit": break

    # Split expression by spaces
    expression = raw_expression.split()
    expression.append("end")

    # build the tree
    built_tree = get_sum(expression)

    # evaluate the tree
    result = evaluate_tree(built_tree)

    print(result)
