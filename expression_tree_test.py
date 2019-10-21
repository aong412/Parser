import pytest
from expression_tree import ExpressionTree, InteriorNode, LeafNode


class TestExpressionTree:

    def test_addition(self):
        left = LeafNode(6)
        right = LeafNode(7)
        root = InteriorNode("+", left, right)
        tree = ExpressionTree(root)
        assert tree.evaluate() == 13, str(tree)

    def test_multiplication(self):
        left = LeafNode(6)
        right = LeafNode(7)
        root = InteriorNode("*", left, right)
        tree = ExpressionTree(root)
        assert tree.evaluate() == 42, str(tree)

    def test_number(self):
        root = LeafNode(150)
        tree = ExpressionTree(root)
        assert tree.evaluate() == 150, str(tree)
