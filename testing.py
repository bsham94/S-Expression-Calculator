import unittest
from lexer import Lexer
from parse import Parser
from parse import Node
import calc


class TestLexer(unittest.TestCase):
    def setUp(self):
        self.lexems = [['multiply', '2', 'add', 'multiply', '2', '3', '8'],
                       ['exponent', '2', 'add', 'multiply', '2', '3', '8'],
                       ['123'],
                       ['']]
        self.tokens = [[[3, 'multiply'], [3, '2'], [3, 'add'], [3, 'multiply'], [3, '2'], [3, '3'], [3, '8']],
                       [[3, '123']], ]

    def test_analyze(self):
        lexer = Lexer()
        tokens = []
        for s in self.lexems[0]:
            token = lexer.analyze(s)
            if token:
                tokens.append(token)
        self.assertEqual(tokens, self.tokens[0])

    def test_analyze_single_number(self):
        lexer = Lexer()
        tokens = []
        for s in self.lexems[2]:
            token = lexer.analyze(s)
            if token:
                tokens.append(token)
        self.assertEqual(tokens, self.tokens[1])

    def test_analyze_empty_string(self):
        lexer = Lexer()
        tokens = []
        with self.assertRaises(Exception):
            for s in self.lexems[3]:
                token = lexer.analyze(s)
                if token:
                    tokens.append(token)

    def test_analyze_invalid_function(self):
        lexer = Lexer()
        tokens = []
        with self.assertRaises(Exception):
            for s in self.lexems[1]:
                token = lexer.analyze(s)
                if token:
                    tokens.append(token)


class TestParser(unittest.TestCase):
    def setUp(self):
        self.tokens = [[3, 'multiply'], [3, '2'], [3, 'add'],
                       [3, 'multiply'], [3, '2'], [3, '3'], [3, '8']]

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 5, "Should be 6")


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.root = Node()
        child1 = Node()
        child1.data = 3
        child2 = Node()
        child2.data = 4
        self.root.children.append(child1)
        self.root.children.append(child2)

    def test_add(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_mul(self):
        self.assertEqual(sum((1, 2, 2)), 5, "Should be 6")


if __name__ == '__main__':
    unittest.main()
