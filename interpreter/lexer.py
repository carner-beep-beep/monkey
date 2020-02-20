import interpreter.token as tok

class Lexer():
    def __init__(self, source):
        self.source = source
        self.position = 0
        self.next_position = 1
        self.c = self.source[self.position]

    def next_token(self):
        c = self.c
        token = None

        if c == '=':
            token = tok.Token(tok.ASSIGN, self.c)
        elif c == '+':
            token = tok.Token(tok.PLUS, self.c)
        elif c == ',':
            token = tok.Token(tok.COMMA, self.c)
        elif c == ';':
            token = tok.Token(tok.SEMICOLON, self.c)
        elif c == '(':
            token = tok.Token(tok.LPAREN, self.c)
        elif c == ')':
            token = tok.Token(tok.RPAREN, self.c)
        elif c == '{':
            token = tok.Token(tok.LBRACE, self.c)
        elif c == '}':
            token = tok.Token(tok.RBRACE, self.c)
        elif c == 0:
            token = tok.Token(tok.EOF, self.c)

        self.read_next_char()
        print(f'position: {self.position} next_position: {self.next_position}')

        return token

    def read_next_char(self):
        if self.next_position >= len(self.source):
            self.c = 0 # tok.EOF
        else:
            self.c = self.source[self.next_position]
        self.position = self.next_position
        self.next_position += 1
