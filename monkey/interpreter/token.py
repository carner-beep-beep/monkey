
# constants
ILLEGAL     = 'ILLEGAL'
EOF         = 'EOF'

IDENT       = 'IDENT'
INT         = 'INT'

ASSIGN      = '='
PLUS        = '+'
MINUS       = '-'
BANG        = '!'
ASTERISK    = '*'
SLASH       = '/'

LT          = '<'
GT          = '>'
EQ          = '=='
NOT_EQ      = '!='

COMMA       = ','
SEMICOLON   = ';'

LPAREN      = '('
RPAREN      = ')'
LBRACE      = '{'
RBRACE      = '}'

# keywords
FUNCTION    = 'FUNCTION'
LET         = 'LET'
TRUE        = 'TRUE'
FALSE       = 'FALSE'
IF          = 'IF'
ELSE        = 'ELSE'
RETURN      = 'RETURN'

keywords = {'fn': FUNCTION, 
            'let': LET,
            'true': TRUE,
            'false': FALSE,
            'if': IF,
            'else': ELSE,
            'return': RETURN}

def lookup_keyword(identifier):
    keyword = keywords.get(identifier)
    if keyword:
        return keyword
    return IDENT

class Token():
    def __init__(self, type=None, literal=None):
        self.type = type
        self.literal = literal

    def __repr__(self):
        return f'[token type: {self.type} literal: {self.literal}]'
