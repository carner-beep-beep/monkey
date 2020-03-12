
class Program():
    def __init__(self):
        self.statements = []

class LetStatement():
    def __init__(self):
        self.token = None
        self.identifier = None
        self.value = None # an expression

    def token_literal(self):
        return self.token.literal

    def __repr__(self):
        return f'LetStatement token: { self.token } identifier: { self.identifier } value: { self.value }'

class ReturnStatement():
    def __init__(self):
        self.token = None
        self.expression = None

    def token_literal(self):
        return self.token.literal

class Identifier():
    def __init__(self, token=None, value=None):
        self.token = token
        self.value = value  # str

    def token_literal():
        return self.token.literal

class ExpressionStatement():
    def __init__(self, token=None, expression=None):
        self.token = token
        self.expression = expression

    def token_literal(self):
        return self.token.literal

class IntegerLiteral():
    def __init__(self, token=None, value=None):
        self.token = token
        self.value = value

    def __repr__(self):
        return self.token.literal

class PrefixExpression():
    def __init__(self, token=None, op=None, expression=None):
        self.token = token
        self.op = op
        self.expression = expression

    def __repr__(self):
        return self.token.literal
