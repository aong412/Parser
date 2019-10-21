#!/usr/bin/python
# Arithmetic Parser for Plexsys by Angela Ong
# Be sure to use Python3+

class Tree:
    """Represents an expression tree."""
    def __init__(self, root):
        self._root = root

    @property
    def root(self):
        return self._root

    def __str__(self):
        return str(self.root)

    def evaluate(self):
        return self._root.evaluate()


class Node:
    """Represents a node in the expression tree.

    This is an abstract class.
    """

    def __init__(self, data, left, right):
        self._data = data
        self._left = left
        self._right = right

    @property
    def data(self):
        return self._data

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    def __str__(self):
        result = ""
        if self.left:
            result += str(self.left)
        if self.right:
            result += str(self.right)
        if self.data:
            result += "%s " % self.data
        return result

    def evaluate(self):
        """Recursively evaluate the expression tree at this node."""
        raise AssertionError("not implemented")


class InteriorNode(Node):
    """Represents an interior (operator) node."""

    def __init__(self, operator, left, right):
        super(operator, left, right)

    def evaluate(self):
        assert self.left and self.right

        left_value = self.left.evaluate()
        right_value = self.right.evaluate()

        # check which operation to apply
        if self.data == '+':
            return left_value + right_value
        elif self.data == '*':
            return left_value * right_value
        else:
            raise ValueError("invalid operator")


class LeafNode(Node):
    """Represents a leaf (term) node."""

    def __init__(self, value):
        super(value, None, None)

    def evaluate(self):
        assert self.data
        return int(self.data)
