#!/usr/bin/python
# Arithmetic Parser for Plexsys by Angela Ong
# Be sure to use Python3+

import pytest
from expression_tree import ExpressionTree, InteriorNode, LeafNode
from parser import Parser


class TestParser:

    def parse_expression(self, expression):
        parser = Parser(expression)
        return parser.parse()

    def evaluate_expression(self, expression):
        tree = self.parse_expression(expression)
        return tree.evaluate()

    def test_addition(self):
        assert self.evaluate_expression("1 + 1") == 2

    def test_multiplication(self):
        assert self.evaluate_expression("2 * 2") == 4

    def test_para_add(self):
        assert self.evaluate_expression("( 1 + 1 )") == 2

    def test_para_mult(self):
        assert self.evaluate_expression("( 2 * 2 )") == 4

    def test_double_digit(self):
        assert self.evaluate_expression("11 + 1") == 12

    def test_para_mult_order(self):
        assert self.evaluate_expression("( 3 + 4 ) * 6") == 42

    def test_para_order(self):
        assert self.evaluate_expression("( 1 + 4 ) * ( 5 + 2 )") == 35

    def test_op_order(self):
        assert self.evaluate_expression("3 + 4 * 6") == 27

    def test_op_order2(self):
        assert self.evaluate_expression("3 * 4 + 6") == 18

    def test_para_order2(self):
        assert self.evaluate_expression("1 * ( 4 + 5 ) * 2") == 18

    def test_para_order3(self):
        assert self.evaluate_expression("1 * 4 + ( 5 * 2 )") == 14

    # def test_bad_para(self):
    #     expression = "( 2 * 2 "
    #     with pytest.raises(ValueError, match='Missing Parenthesis'):
    #         self.evaluate_tree(self.build_tree(expression))
    #
    # def test_bad_char(self):
    #     expression = "&"
    #     with pytest.raises(ValueError, match='Bad Format'):
    #         self.evaluate_tree(self.build_tree(expression))
    #
    # def test_missing_operand(self):
    #     expression = "22 + "
    #     assert self.evaluate_tree(self.build_tree(expression)) is 22
    #
    # def test_bad_operator(self):
    #     expression = "2 & 3 "
    #     with pytest.raises(ValueError, match='Bad Format'):
    #         self.evaluate_tree(self.build_tree(expression))
    #
    # def test_missing_operands(self):
    #     expression = "+"
    #     with pytest.raises(ValueError, match='Bad Format'):
    #         self.evaluate_tree(self.build_tree(expression))
