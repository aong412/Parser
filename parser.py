#!/usr/bin/python
# Arithmetic Parser for Plexsys by Angela Ong
# Be sure to use Python3+

from expression_tree import ExpressionTree, InteriorNode, LeafNode


class Parser:
    """Parses an arithmetic expression as specified by interviewer."""

    def __init__(self, expression):
        self._expression = expression
        self._parsed_value = None
        self._tokens = None

    @property
    def expression(self):
        """Returns the expression provided to the parser."""
        return self._expression

    def _tokenize(self):
        """Tokenizes expression into self._tokens."""
        tokens = []
        index = 0
        while index < len(self._expression):
            c = self._expression[index]
            if c.isspace():
                pass
            elif c in "+*()":
                tokens.append(c)
            elif c.isdigit():
                value = int(c)
                if tokens and isinstance(tokens[-1], int):
                    tokens[-1] = tokens[-1] * 10 + value
                else:
                    tokens.append(value)
            else:
                self._report_syntax_error("unexpected token at index %d: %s" % (index, c))
            index += 1
        self._tokens = tokens

    def _pop_token(self, expected):
        """Pops the expected character from self._tokens if matching.

        Returns:
            True if expected matches the next token, False otherwise.
        """
        if self._tokens and self._tokens[0] == expected:
            del self._tokens[0]
            return True
        else:
            return False

    def _next_token(self):
        """Returns the next token in self._tokens."""
        if not self._tokens:
            return None
        return self._tokens[0]

    def _report_syntax_error(self, message):
        """Raises a syntax error with message."""
        raise ValueError("syntax error: %s" % message)

    def _report_syntax_error_at_next_token(self):
        """Raises a syntax error at next token."""
        if self._tokens:
            raise self._report_syntax_error("unexpected token: %s" % self._next_token())
        raise self._report_syntax_error("unexpected end of expression")

    def _parse_next_term(self):
        """Parses either a bracketed group or a number."""
        if self._pop_token('('):
            node = self._parse_next_sum()
            if not self._pop_token(')'):
                self._report_syntax_error('missing parenthesis')
            return node
        token = self._next_token()
        if isinstance(token, int):
            del self._tokens[0]
            return LeafNode(token)
        self._report_syntax_error_at_next_token()

    def _parse_next_sum(self):
        """Parses a potential sum."""
        # Products have greater precedence.
        term = self._parse_next_product()
        if self._pop_token('+'):
            expr = self._parse_next_sum()
            return InteriorNode('+', term, expr)
        return term

    def _parse_next_product(self):
        """Parses a potential product."""
        term = self._parse_next_term()
        if self._pop_token('*'):
            expr = self._parse_next_product()
            return InteriorNode('*', term, expr)
        return term

    def parse(self):
        """Parses the given expression and returns an ExpressionTree.

        Returns:
            An ExpressionTree of the provided expression.
        Raises:
            ValueError on invalid syntax.
        """
        if self._parsed_value:
            return self._parsed_value
        self._tokenize()
        # Entry point is self._parse_next_sum() because we want to
        # obey operator precedence, and the sum parser first tries
        # to parse a product.
        root = self._parse_next_sum()
        self._parsed_value = ExpressionTree(root)
        return self._parsed_value
