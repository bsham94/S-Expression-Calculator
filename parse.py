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
        '''
        Breaks input into seperate strings
        '''
        self.sexp = self.sexp.split(' ')
        temp_sexp = []
        for s in self.sexp:
            temp_lexeme = []
            l_bracket = []
            r_bracket = []
            # Seperates the left and right brackets from the digits and functions
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
        '''
        Performs setup for the parser
        '''
        self.tokenize()
        for s in self.sexp:
            # Creates a pair of values to represent a token
            # [TokenType, Value]
            token = self.lexer.analyze(s)
            if token:
                self.tokens.append(token)

    def parse(self):
        '''
        Parses the list of tokens and builds a syntax tree
        '''
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
                    if not stack:
                        current_state = self.ERROR
                    # State machine for processing a token
                    while current_state != self.END:
                        if current_state == self.STARTEXP:
                            current_state = self.startexp_state(stack, token)
                        elif current_state == self.START:
                            current_state = token[0]
                        elif current_state == self.EXPRESSION:
                            current_state = self.expression_state(token)
                        elif current_state == self.LBRACKET:
                            current_state = self.lbracket_state(stack)
                        elif current_state == self.RBRACKET:
                            current_state = self.rbracket_state(stack)
                        elif current_state == self.DIGIT:
                            current_state = self.digit_state(stack, token)
                        elif current_state == self.FUNCTION:
                            current_state = self.function_state(
                                stack, token)
                        elif current_state == self.ERROR:
                            raise Exception(
                                "Invalid number of function parameters.\nEach function requires 2 parameters.")
                    current_state = self.START
        return root

    def startexp_state(self, stack, token):
        '''
        Logic for startexpression state
        '''
        current_state = token[0]
        if current_state == self.LBRACKET:
            current_state = self.END
        elif current_state == self.EXPRESSION:
            if token[1].isdigit():
                stack[-1].data = token[1]
                current_state = self.END
        return current_state

    def rbracket_state(self, stack):
        '''
        Logic for rightbracket state
        '''
        # Sets state to error if node has more than 2 children
        if len(stack[-1].children) == 2:
            # Rbracket indicates end of an expression
            # Pop node off the stack
            stack.pop()
            return self.END
        else:
            return self.ERROR

    def lbracket_state(self, stack):
        '''
        Logic for leftbracket state
        stack: datastructure holding the tree nodes
        return: the new state
        '''
        # Sets state to error if node has more than 2 children
        if len(stack[-1].children) < 2:
            # Lbracket means new expression
            # Add node to stack
            node = Node()
            stack[-1].children.append(node)
            stack.append(node)
            return self.END
        else:
            return self.ERROR

    def expression_state(self, token):
        '''
        Logic for expression state
        token: current token being processed
        return: the new state
        '''
        current_state = None
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
        '''
        Logic for digit state
        stack: datastructure holding the tree nodes
        token: current token being processed
        return: the new state
        '''
        # Sets state to error if node has more than 2 children
        if len(stack[-1].children) < 2:
            node = Node()
            node.data = token[1]
            # Add a new node to list
            stack[-1].children.append(node)
            return self.END
        else:
            return self.ERROR

    def function_state(self, stack, token):
        '''
        Logic for expression state
        stack: datastructure holding the tree nodes
        token: current token being processed
        return: the new state
        '''
        # Sets node data to either "Add" or "Multiply"
        stack[-1].data = token[1]
        return self.END
