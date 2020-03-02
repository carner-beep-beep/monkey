from monkey.interpreter.lexer import Lexer
from monkey.interpreter.parser import Parser

def test_let_statements():
    program_input = '''let x = 5;
        let y = 10;
        let foobar = 838383;'''

    l = Lexer(program_input)
    parser = Parser(l)

    program = parser.parse_program()

    assert program != None

    assert len(program.statements) == 3

    expected_idents = ['x', 'y', 'foobar']
    for i, statement in enumerate(program.statements):
        assert statement.token_literal() == 'let'
        assert statement.identifier.value == expected_idents[i]

def test_return_statements():
    program_input = '''return 4;
    return 5;
    return four * five;'''

    l = Lexer(program_input)
    p = Parser(l)

    program = p.parse_program()

    assert program != None
    assert len(program.statements) == 3

    for statement in program.statements:
        assert statement.token_literal() == 'return'

