from monkey.interpreter.ast import Program, LetStatement, Identifier
from monkey.interpreter import token

class Parser():
    def __init__(self, lexer):
        self.lexer = lexer
        self.cur_token = None
        self.peek_token = None
        self.errors = []

        self.next_token()
        self.next_token()

    def next_token(self):
        self.cur_token = self.peek_token
        self.peek_token = self.lexer.next_token()
        print(f'cur_token: {self.cur_token} peek_token: {self.peek_token}')

    def parse_program(self):
        program = Program()

        while self.cur_token.type != token.EOF:
            print('in parse program loop!')
            stmt = self.parse_statement()
            print(f'Stmt: {stmt}')
            if stmt != None:
                program.statements.append(stmt)
                print(f'Statements: { program.statements }')

            self.next_token()
        return program

    def parse_statement(self):
        if self.cur_token.type == token.LET:
            return self.parse_let_statement()
        elif self.cur_token.type == token.RETURN:
            return self.parse_return_statement()
        else:
            return None

    def parse_let_statement(self):
        print('in parse let statement')
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
            print('looping!!')
            self.next_token()
        
        print(f'let_stmt: {let_stmt}')
        return let_stmt

    def parse_return_statement(self):
        pass

    def cur_token_is(self, tok_type):
        return self.cur_token.type == tok_type

    def expect_peek(self, tok_type):
        if self.peek_token.type == tok_type:
            return True
        else:
            self.errors.append(f'Expected: { tok_type } Got: { self.peek_token.type }')
            return False

