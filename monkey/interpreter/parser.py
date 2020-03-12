from monkey.interpreter.ast import Program, LetStatement, Identifier, ReturnStatement, \
        ExpressionStatement, IntegerLiteral, PrefixExpression
from monkey.interpreter import token

# precedence - order of op
LOWEST = 0
EQUALS = 1
LESSGREATER = 2
SUM = 3
PRODUCT = 4
PREFIX = 5
CALL = 6

class Parser():
    def __init__(self, lexer):
        self.lexer = lexer
        self.cur_token = None
        self.peek_token = None
        self.errors = []
        self.prefixParseFns = {}
        self.infixParseFns = {}
        self.precedences = { token.EQ: EQUALS,
                             token.NOT_EQ: EQUALS,
                             token.LT: LESSGREATER,
                             token.GT: LESSGREATER,
                             token.PLUS: SUM,
                             token.MINUS: SUM,
                             token.SLASH: PRODUCT,
                             token.ASTERISK: PRODUCT }

        self.next_token()
        self.next_token()

        self.registerParseFn('prefix', token.IDENT, self.parse_identifier)
        self.registerParseFn('prefix', token.INT, self.parse_integer_literal)
        self.registerParseFn('prefix', token.BANG, self.parse_prefix_expression)
        self.registerParseFn('prefix', token.MINUS, self.parse_prefix_expression)

        self.registerParseFn('infix', token.PLUS, self.parse_infix_expression)
        self.registerParseFn('infix', token.MINUS, self.parse_infix_expression)
        self.registerParseFn('infix', token.SLASH, self.parse_infix_expression)
        self.registerParseFn('infix', token.ASTERISK, self.parse_infix_expression)
        self.registerParseFn('infix', token.EQ, self.parse_infix_expression)
        self.registerParseFn('infix', token.NOT_EQ, self.parse_infix_expression)
        self.registerParseFn('infix', token.LT, self.parse_infix_expression)
        self.registerParseFn('infix', token.GT, self.parse_infix_expression)


    def registerParseFn(self, parse_type, token_type, fn):
        if parse_type == 'prefix':
            self.prefixParseFns[token_type] = fn
        elif parse_type == 'infix':
            self.infixParseFns[token_type] = fn

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
            return self.parse_expression_statement()

    def parse_expression_statement(self):
        print(f'### parse_expression_statement: {self.cur_token}')
        stmt = ExpressionStatement(token=self.cur_token)

        stmt.expression = self.parse_expression(LOWEST)
        
        print(f'### parse_expression_statement peek: {self.peek_token}')
        if self.peek_token.type == token.SEMICOLON:
            self.next_token()
        
        print(f'### parse_expression_statement end: {self.cur_token}')
        return stmt

    def parse_expression(self, precedence):
        prefix = self.prefixParseFns[self.cur_token.type]
        print(f'### parse_expression: {prefix}')
        if prefix == None:
            self.errors.append(f'no prefix parse function found for: {self.cur_token.type}')
            return None

        leftExp = prefix()
        return leftExp

    def parse_identifier(self):
        ident = Identifier(token=self.cur_token)
        ident.value = ident.token.literal

        print(f'### parse_identifier: {ident}')

        return ident

    def parse_integer_literal(self):
        lit = IntegerLiteral(token=self.cur_token)
        lit.value = int(lit.token.literal)
        
        print(f'### parse_integer_literal: {lit}')
        return lit
    
    def parse_prefix_expression(self):
        expr = PrefixExpression(token=self.cur_token)
        expr.op = expr.token.literal

        self.next_token()
        print(f'### parse_prefix_expression: {expr}')
        expr.expression = self.parse_expression(PREFIX)

        return expr

    def parse_infix_expression(self, left_expr):
        expr = InfixExpression(token=self.cur_token)
        expr.left_expr = left_expr
        expr.op = expr.token.literal

        precedence = self.cur_precedence()
        self.next_token()
        expr.right = self.parse_expression(precedence)

        return expr

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
        return_stmt = ReturnStatement()
        return_stmt.token = self.cur_token

        self.next_token()

        while not self.cur_token_is(token.SEMICOLON):
            print('looping!')
            self.next_token()

        return return_stmt

    def cur_token_is(self, tok_type):
        return self.cur_token.type == tok_type

    def expect_peek(self, tok_type):
        if self.peek_token.type == tok_type:
            return True
        else:
            self.errors.append(f'Expected: { tok_type } Got: { self.peek_token.type }')
            return False

    def peek_precedence(self):
        prec = self.precedences[self.peek_token.type]
        if prec:
            return prec
        return LOWEST

    def cur_precedence(self):
        prec = self.precedences[self.cur_token.type]
        if prec:
            return prec
        return LOWEST

