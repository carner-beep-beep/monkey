
# constants
ILLEGAL     = 'ILLEGAL'
EOF         = 'EOF'

IDENT       = 'IDENT'
INT         = 'INT'

ASSIGN      = '='
PLUS        = '+'

COMMA       = ','
SEMICOLON   = ';'

LPAREN      = '('
RPAREN      = ')'
LBRACE      = '{'
RBRACE      = '}'

# keywords
FUNCTION    = 'FUNCTION'
LET         = 'LET'

class Token():
    def __init__(self, type=None, literal=None):
        self.type = type
        self.literal = literal

    def __repr__(self):
        return f'[token type: {self.type} literal: {self.literal}]'
