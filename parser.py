#!/usr/bin/python
# Arithmetic Parser for Plexsys by Angela Ong
# Be sure to use Python3+


# Tree class
class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)


# preorder tree printing
def print_tree(tree):
    if tree is None: return
    print(tree.cargo)
    print_tree(tree.left)
    print_tree(tree.right)


# confirm token operator validity
def validate(token):
    if token.isdigit() or token == '(' or token == ')' or token == '+' or \
        token == '*' or token == 'end': return True
    else: raise ValueError('Bad Format')


# handle operands
def get_number(exp_list):
    if match(exp_list, '('):
        x = get_sum(exp_list)
        if not match(exp_list, ')'):
            raise ValueError('Missing Parenthesis')
        return x
    else:
        x = exp_list[0]
        if x.isdigit():
            exp_list[0:1] = []
            return Tree(x, None, None)

        if validate(x): return None


# build tree for sums; products before sums ****
def get_sum(exp_list):
    a = get_product(exp_list)
    if match(exp_list, '+'):
        b = get_sum(exp_list)
        return Tree('+', a, b)
    if validate(exp_list[0]): return a


# build tree for products
def get_product(exp_list):
    a = get_number(exp_list)
    if match(exp_list, '*'):
        b = get_product(exp_list)
        return Tree('*', a, b)
    if validate(exp_list[0]): return a


# match for expected character and pop from list
def match(exp_list, expected):
    if exp_list[0] == expected:
        del exp_list[0]
        return True
    else:
        return False


# use recursion to get arithmetic result of tree
def evaluate_tree(root):
    # empty tree
    if root is None:
        return 0

    # leaf node
    if root.left is None and root.right is None:
        # bug here if the expression string is "+/*/)"
        return int(root.cargo)

    # evaluate left tree
    left_sum = evaluate_tree(root.left)

    # evaluate right tree
    right_sum = evaluate_tree(root.right)

    # check which operation to apply
    if root.cargo == '+':
        return left_sum + right_sum
    elif root.cargo == '*':
        return left_sum * right_sum
    else:
        raise ValueError('Operator not found')
