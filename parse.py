from lexer import Lexer


class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
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
        self.LBRACKET = 8
        self.END = 9
        self.ERROR = 10

    def tokenize(self):
        self.sexp = self.sexp.replace("(", "").replace(")", "")
        self.sexp = self.sexp.split(' ')

    def setup(self):
        self.tokenize()
        for s in self.sexp:
            token = self.lexer.analyze(s)
            if token:
                self.tokens.append(token)

    def parse(self):
        self.setup()
        root = Node()
        if self.tokens:
            stack = [root]
            for token in self.tokens:
                current_state = self.START
                temp = token
                curr = stack.pop()
                while current_state != self.END:
                    if current_state == self.START:
                        current_state = token[0]
                    elif current_state == self.EXPRESSION:
                        if temp[1] == 'multiply':
                            temp[0] = self.MULTIPLY
                            current_state = self.FUNCTION
                        elif temp[1] == 'add':
                            temp[0] = self.ADD
                            current_state = self.FUNCTION
                        else:
                            temp[0] = self.DIGIT
                            current_state = self.DIGIT
                    # Digit
                    elif current_state == self.DIGIT:
                        curr.data = temp[1]
                        current_state = self.END
                    # Function
                    elif current_state == self.FUNCTION:
                        curr.data = temp[1]
                        curr.right = Node()
                        curr.left = Node()
                        stack.append(curr.right)
                        stack.append(curr.left)
                        current_state = self.END
        return root
