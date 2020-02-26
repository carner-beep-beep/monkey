from monkey.interpreter.ast import Program, LetStatement, Identifier
from monkey.interpreter import token

class Parser():
    def __init__(self, lexer):
        self.lexer = lexer
        self.cur_token = None
        self.peek_token = None

        self.next_token()
        self.next_token()

    def next_token(self):
        self.cur_token = self.peek_token
        self.peek_token = self.lexer.next_token()

    def parse_program(self):
        program = Program()

        while self.cur_token != token.EOF:
            stmt = self.parse_statement()
            if stmt != None:
                program.statements.append(stmt)

            self.next_token()
        return program

    def parse_statement(self):
        if self.cur_token.type == token.LET:
            self.parse_let_statement()
        else:
            return None

    def parse_let_statement(self):
        let_stmt = LetStatement()
        let_stmt.token = self.cur_token
        
        # messy
        if not self.expect_peek(token.IDENT):
            return None
        self.next_token()

        let_stmt.identifier = Identifier(token=self.cur_token,
                value=self.cur_token.literal)
        
        # :(
        if not self.expect_peek(token.ASSIGN):
            return None
        self.next_token()

        #let_stmt.value = self.parse_expression()
        
        # temp
        while not self.cur_token_is(token.SEMICOLON):
            self.next_token()

        return let_stmt

    def cur_token_is(self, tok_type):
        return self.cur_token.type == tok_type

    def expect_peek(self, tok_type):
        return self.peek_token.type == tok_type

