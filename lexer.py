class Lexer:
    def __init__(self):
        self.functions = ['add', 'multiply']
        self.DIGIT = 1
        self.FUNCTION = 2
        self.EXPRESSION = 3

    def analyze(self, lexeme):
        token = []
        if lexeme[0]:
            current_state = self.DIGIT if lexeme[0].isdigit(
            ) else self.FUNCTION
        if current_state == self.DIGIT:
            # token = ['INTEGER', lexeme] if lexeme.isdigit() else []
            token = [self.EXPRESSION, lexeme] if lexeme.isdigit() else []
        if current_state == self.FUNCTION:
            token = [self.EXPRESSION, lexeme] if lexeme.lower(
            ) in self.functions else []
        if not token:
            raise TypeError("Unrecognized function")
        return token
