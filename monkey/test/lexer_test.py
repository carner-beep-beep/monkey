from monkey.interpreter import token
from monkey.interpreter import lexer


def test_lexer():
    program_input = '''let five = 5;
        let ten = 10;

        let add = fn(x, y) {
            x + y;
        };

        let result = add(five, ten);'''

    l = lexer.Lexer(program_input)

    expected_tokens = [
            (token.LET, 'let'),
            (token.IDENT, 'five'),
            (token.ASSIGN, '='),
            (token.INT, '5'),
            (token.SEMICOLON, ';'),
            (token.LET, 'let'),
            (token.IDENT, 'ten'),
            (token.ASSIGN, '='),
            (token.INT, '10'),
            (token.SEMICOLON, ';'),
            (token.LET, 'let'),
            (token.IDENT, 'add'),
            (token.ASSIGN, '='),
            (token.FUNCTION, 'fn'),
            (token.LPAREN, '('),
            (token.IDENT, 'x'),
            (token.COMMA, ','),
            (token.IDENT, 'y'),
            (token.RPAREN, ')'),
            (token.LBRACE, '{'),
            (token.IDENT, 'x'),
            (token.PLUS, '+'),
            (token.IDENT, 'y'),
            (token.SEMICOLON, ';'),
            (token.RBRACE, '}'),
            (token.SEMICOLON, ';'),
            (token.LET, 'let'),
            (token.IDENT, 'result'),
            (token.ASSIGN, '='),
            (token.IDENT, 'add'),
            (token.LPAREN, '('),
            (token.IDENT, 'five'),
            (token.COMMA, ','),
            (token.IDENT, 'ten'),
            (token.RPAREN, ')'),
            (token.SEMICOLON, ';'),
            (token.EOF, '0')
            ]

    for expected_token in expected_tokens:
        tok = l.next_token()

        assert tok.type == expected_token[0], f'got: {tok.type}, expected: {expected_token[0]}'

        assert tok.literal == expected_token[1], 'token literals not matching' 