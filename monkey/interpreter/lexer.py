from monkey.interpreter import token as tok

class Lexer():
    def __init__(self, source):
        self.source = source
        self.position = 0
        self.next_position = 1
        self.c = self.source[self.position]

    def next_token(self):
        token = None

        self.skip_whitespace()
        #print(f'next_token start: c = {self.c}, type = {type(self.c)}, len = {len(self.c)}')

        #print(f"conditional { self.c == '=' }")
        print(f'current char: {self.c}')

        if self.c == '=':
            if self.peek_char() == '=':
                c = self.c
                self.read_next_char()
                token = tok.Token(tok.EQ, c + self.c)
            else:
                token = tok.Token(tok.ASSIGN, self.c)
        elif self.c == '+':
            token = tok.Token(tok.PLUS, self.c)
        elif self.c == '-':
            token = tok.Token(tok.MINUS, self.c)
        elif self.c == '!':
            if self.peek_char() == '=':
                c = self.c
                self.read_next_char()
                token = tok.Token(tok.NOT_EQ, c + self.c)
            else:
                token = tok.Token(tok.BANG, self.c)
        elif self.c == '*':
            token = tok.Token(tok.ASTERISK, self.c)
        elif self.c == '/':
            token = tok.Token(tok.SLASH, self.c)
        elif self.c == '<':
            token = tok.Token(tok.LT, self.c)
        elif self.c == '>':
            token = tok.Token(tok.GT, self.c)
        elif self.c == ',':
            token = tok.Token(tok.COMMA, self.c)
        elif self.c == ';':
            token = tok.Token(tok.SEMICOLON, self.c)
        elif self.c == '(':
            token = tok.Token(tok.LPAREN, self.c)
        elif self.c == ')':
            token = tok.Token(tok.RPAREN, self.c)
        elif self.c == '{':
            token = tok.Token(tok.LBRACE, self.c)
        elif self.c == '}':
            token = tok.Token(tok.RBRACE, self.c)
        elif self.c == 0:
            token = tok.Token(tok.EOF, str(0))
        else:
            print(f'In else statement {self.c}')
            if self.c.isalpha():
                literal = self.read_identifier()
                tok_type = tok.lookup_keyword(literal)
                #print(f'identifier literal: {literal}, type: {tok_type}')
                print(tok_type, literal)
                return tok.Token(tok_type, literal) # already called read_next_char to build ident
            elif self.c.isdigit():
                literal = self.read_number()
                tok_type = tok.INT
                print(tok_type, literal)
                return tok.Token(tok_type, literal)
            else:
                #print(f'in ILLEGAL else with {self.c}:{type(self.c)}')
                print(f'in illegal with {self.c} {type(self.c)}')
                token = tok.Token(tok.ILLEGAL, self.c)

        self.read_next_char()
        #print(f'position: {self.position} next_position: {self.next_position}')
        
        print(token)
        return token

    def read_next_char(self):
        if self.next_position >= len(self.source):
            self.c = 0 # tok.EOF
        else:
            self.c = self.source[self.next_position]
        self.position = self.next_position
        self.next_position += 1

    def read_identifier(self):
        start_position = self.position
        while self.c.isalpha() or self.c == '_':
            self.read_next_char()
        return self.source[start_position:self.position]

    def read_number(self):
        start_position = self.position
        while self.c.isdigit():
            self.read_next_char()
        return self.source[start_position:self.position]

    def skip_whitespace(self):
        if isinstance(self.c, str):
            while isinstance(self.c, str) and self.c.isspace():
                self.read_next_char()

    def peek_char(self):
        if self.next_position >= len(self.source):
            return 0
        else:
            return self.source[self.next_position]
