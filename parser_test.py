#!/usr/bin/python
# Arithmetic Parser for Plexsys by Angela Ong
# Be sure to use Python3+

import pytest
from parser import Parser


class TestParser:

    def parse_expression(self, expression):
        parser = Parser(expression)
        return parser.parse()

    def evaluate_expression(self, expression):
        tree = self.parse_expression(expression)
        return tree.evaluate()

    def test_addition(self):
        assert self.evaluate_expression("1+1") == 2

    def test_multiplication(self):
        assert self.evaluate_expression("2*2") == 4

    def test_para_add(self):
        assert self.evaluate_expression("(1+1)") == 2

    def test_para_mult(self):
        assert self.evaluate_expression("(2*2)") == 4

    def test_double_digit(self):
        assert self.evaluate_expression("11+1") == 12

    def test_para_mult_order(self):
        assert self.evaluate_expression("(3+4)*6") == 42

    def test_para_order(self):
        assert self.evaluate_expression("(1+4)*(5+2)") == 35

    def test_op_order(self):
        assert self.evaluate_expression("3+4*6") == 27

    def test_op_order2(self):
        assert self.evaluate_expression("3*4 + 6*8") == 60

    def test_para_order2(self):
        assert self.evaluate_expression("1 * (4+5) * 2") == 18

    def test_para_order3(self):
        assert self.evaluate_expression("1*4 + (5*(2*13))") == 134

    def test_bad_para(self):
        with pytest.raises(ValueError, match='syntax error: missing parenthesis'):
            self.evaluate_expression("(2 * 2 ")

    def test_bad_char(self):
        with pytest.raises(ValueError, match='syntax error: unexpected token at index 0: &'):
            self.evaluate_expression("&")

    def test_missing_operand(self):
        with pytest.raises(ValueError, match='syntax error: unexpected end of expression'):
            self.evaluate_expression("22 +")

    def test_missing_operand2(self):
        with pytest.raises(ValueError, match='syntax error: unexpected token: +'):
            self.evaluate_expression("+ 22")

    def test_bad_operator(self):
        with pytest.raises(ValueError, match='syntax error: unexpected token at index 2: &'):
            self.evaluate_expression("2 & 3")

    def test_missing_operands(self):
        with pytest.raises(ValueError, match='syntax error: unexpected token: +'):
            self.evaluate_expression("+")
