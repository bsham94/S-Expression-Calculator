from doctest import Example


class Lexer:
    def __init__(self):
        self.functions = ['add', 'multiply']
        self.START = 0
        self.DIGIT = 1
        self.FUNCTION = 2
        self.EXPRESSION = 3
        self.LBRACKET = 7
        self.RBRACKET = 8

    def analyze(self, lexeme):
        token = []
        current_state = self.START
        if lexeme and lexeme[0]:
            if lexeme[0].isdigit():
                current_state = self.DIGIT
            elif lexeme == ')':
                current_state = self.RBRACKET
            elif lexeme == '(':
                current_state = self.LBRACKET
            else:
                current_state = self.FUNCTION
        if current_state == self.DIGIT or current_state == self.FUNCTION:
            token = [self.EXPRESSION, lexeme] if lexeme.isdigit() or lexeme.lower(
            ) in self.functions else []
        elif current_state == self.RBRACKET:
            token = [self.RBRACKET, lexeme]
        elif current_state == self.LBRACKET:
            token = [self.LBRACKET, lexeme]
        if not token:
            raise Exception("Unrecognized function.")
        return token
