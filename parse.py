from typing import Type
from lexer import Lexer


class Node:
    def __init__(self, data=None):
        self.data = data
        self.children = []


class Parser:
    def __init__(self, sexp):
        self.sexp = sexp
        self.lexer = Lexer()
        self.tokens = []
        self.START = 0
        self.DIGIT = 1
        self.EXPRESSION = 3
        self.ADD = 4
        self.MULTIPLY = 5
        self.FUNCTION = 6
        self.LBRACKET = 7
        self.RBRACKET = 8
        self.END = 9
        self.ERROR = 10
        self.STARTEXP = 11

    def tokenize(self):
        self.sexp = self.sexp.split(' ')
        temp_sexp = []
        for s in self.sexp:
            temp_lexeme = []
            l_bracket = []
            r_bracket = []
            for c in s:
                if c == ")":
                    r_bracket.append(")")
                elif c == "(":
                    l_bracket.append("(")
                else:
                    temp_lexeme.append(c)
            if l_bracket:
                for l in l_bracket:
                    temp_sexp.append(l)
            if temp_lexeme:
                temp_sexp.append(''.join(temp_lexeme))
            if r_bracket:
                for r in r_bracket:
                    temp_sexp.append(r)
        self.sexp = temp_sexp

    def setup(self):
        self.tokenize()
        for s in self.sexp:
            token = self.lexer.analyze(s)
            if token:
                self.tokens.append(token)

    # START = EXPR
    # EXPR = INTEGER | FUNC
    # FUNC = ADD | MULTIPLY
    # INTEGER = DIGIT, {DIGIT}
    # DIGIT = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
    # ADD = "(", "a", "d", "d", " ", EXPR, " ", EXPR, ")"
    # MULTIPLY = "(", "m", "u", "l", "t", "i", "p", "l", "y", " ", EXPR, " ", EXPR, ")"
    def parse(self):
        root = Node()
        current_state = self.STARTEXP
        try:
            self.setup()
        except Exception as e:
            raise e
        else:
            if self.tokens:
                stack = [root]
                for token in self.tokens:
                    temp = token
                    if not stack:
                        current_state = self.ERROR
                    while current_state != self.END:
                        if current_state == self.STARTEXP:
                            current_state = self.startexp_state(stack, temp)
                        elif current_state == self.START:
                            current_state = token[0]
                        elif current_state == self.EXPRESSION:
                            current_state = self.expression_state(token)
                        elif current_state == self.LBRACKET:
                            current_state = self.lbracket_state(stack)
                        elif current_state == self.RBRACKET:
                            current_state = self.rbracket_state(stack)
                        elif current_state == self.DIGIT:
                            current_state = self.digit_state(stack, temp)
                        elif current_state == self.FUNCTION:
                            current_state = self.function_state(
                                stack, temp)
                        elif current_state == self.ERROR:
                            raise Exception(
                                "Invalid number of function parameters.\nEach function requires 2 parameters.")
                    current_state = self.START
        return root

    def startexp_state(self, stack, token):
        current_state = token[0]
        if current_state == self.LBRACKET:
            current_state = self.END
        elif current_state == self.EXPRESSION:
            if token[1].isdigit():
                stack[-1].data = token[1]
                current_state = self.END
        return current_state

    def rbracket_state(self, stack):
        if len(stack[-1].children) == 2:
            stack.pop()
            return self.END
        else:
            return self.ERROR

    def lbracket_state(self, stack):
        if len(stack[-1].children) < 2:
            node = Node()
            stack[-1].children.append(node)
            stack.append(node)
        else:
            return self.ERROR
        return self.END

    def expression_state(self, token):
        current_state = -1
        if token[1] == 'multiply':
            token[0] = self.MULTIPLY
            current_state = self.FUNCTION
        elif token[1] == 'add':
            token[0] = self.ADD
            current_state = self.FUNCTION
        elif token[1].isdigit():
            token[0] = self.DIGIT
            current_state = self.DIGIT
        else:
            current_state = self.ERROR
        return current_state

    def digit_state(self, stack, token):
        if len(stack[-1].children) < 2:
            node = Node()
            node.data = token[1]
            stack[-1].children.append(node)
        else:
            return self.ERROR
        return self.END

    def function_state(self, stack, token):
        stack[-1].data = token[1]
        return self.END
