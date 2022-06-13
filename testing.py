import unittest

from lexer import Lexer


class TestLexer(unittest.TestCase):
    def setUp(self):
        self.lexer = Lexer()
        self.lexems = [['multiply', '2', 'add', 'multiply', '2', '3', '8'],
                       ['exponent', '2', 'add', 'multiply', '2', '3', '8'],
                       ['123'],
                       ['']]
        self.tokens = [[[3, 'multiply'], [3, '2'], [3, 'add'], [3, 'multiply'], [3, '2'], [3, '3'], [3, '8']],
                       [[3, '123']], ]

    def test_analyze(self):
        tokens = []
        for s in self.lexems[0]:
            token = self.lexer.analyze(s)
            if token:
                tokens.append(token)
        self.assertEqual(tokens, self.tokens[0])

    def test_analyze_single_number(self):
        tokens = []
        for s in self.lexems[2]:
            token = self.lexer.analyze(s)
            if token:
                tokens.append(token)
        self.assertEqual(tokens, self.tokens[1])

    def test_analyze_empty_string(self):
        tokens = []
        with self.assertRaises(Exception):
            for s in self.lexems[3]:
                token = self.lexer.analyze(s)
                if token:
                    tokens.append(token)

    def test_analyze_invalid_function(self):
        tokens = []
        with self.assertRaises(Exception):
            for s in self.lexems[1]:
                token = self.lexer.analyze(s)
                if token:
                    tokens.append(token)


if __name__ == '__main__':
    unittest.main()
