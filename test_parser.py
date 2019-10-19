import pytest
from Parser import get_sum, evaluate_tree


class TestParser:

    def build_tree(self, expression):
        x = expression.split()
        x.append("end")
        return get_sum(x)

    def evaluate_tree(self, built_tree):
        return evaluate_tree(built_tree)

    def test_addition(self):
        expression = "1 + 1"
        assert self.evaluate_tree(self.build_tree(expression)) is 2

    def test_multiply(self):
        expression = "2 * 2"
        assert self.evaluate_tree(self.build_tree(expression)) is 4

    def test_para_add(self):
        expression = "( 1 + 1 )"
        assert self.evaluate_tree(self.build_tree(expression)) is 2

    def test_para_mult(self):
        expression = "( 2 * 2 )"
        assert self.evaluate_tree(self.build_tree(expression)) is 4

    def test_double_digit(self):
        expression = "11 + 1"
        assert self.evaluate_tree(self.build_tree(expression)) is 12

    def test_para_mult_order(self):
        expression = "( 3 + 4 ) * 6"
        assert self.evaluate_tree(self.build_tree(expression)) is 42

    def test_para_order(self):
        expression = "( 1 + 4 ) * ( 5 + 2 )"
        assert self.evaluate_tree(self.build_tree(expression)) is 35

    def test_op_order(self):
        expression = "3 + 4 * 6"
        assert self.evaluate_tree(self.build_tree(expression)) is 27

    def test_op_order2(self):
        expression = "3 * 4 + 6"
        assert self.evaluate_tree(self.build_tree(expression)) is 18

    def test_para_order2(self):
        expression = "1 * ( 4 + 5 ) * 2"
        assert self.evaluate_tree(self.build_tree(expression)) is 18

    def test_para_order3(self):
        expression = "1 * 4 + ( 5 * 2 )"
        assert self.evaluate_tree(self.build_tree(expression)) is 14

    def test_bad_para(self):
        expression = "( 2 * 2 "
        with pytest.raises(ValueError, match='Missing Parenthesis'):
            self.evaluate_tree(self.build_tree(expression))

    def test_bad_char(self):
        expression = "&"
        with pytest.raises(ValueError, match='Bad Format'):
            self.evaluate_tree(self.build_tree(expression))

    def test_missing_operand(self):
        expression = "22 + "
        assert self.evaluate_tree(self.build_tree(expression)) is 22

    def test_bad_operator(self):
        expression = "2 & 3 "
        with pytest.raises(ValueError, match='Bad Format'):
            self.evaluate_tree(self.build_tree(expression))

    def test_missing_operands(self):
        expression = "+"
        with pytest.raises(ValueError, match='Bad Format'):
            self.evaluate_tree(self.build_tree(expression))
