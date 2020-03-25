from monkey.interpreter import token
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

def test_identifier_expression():
    program_in = 'foobar;'

    l = Lexer(program_in)
    p = Parser(l)

    program = p.parse_program()

    assert program != None

    assert len(program.statements) == 1

    expr_stmt = program.statements[0]
    print(expr_stmt)

    assert expr_stmt.token.type == token.IDENT
    assert expr_stmt.token_literal() == 'foobar'

def test_integer_literal_expression():
    program_in = '1234;'
    l = Lexer(program_in)
    p = Parser(l)

    program = p.parse_program()

    assert program != None

    assert len(program.statements) == 1

    expr_stmt = program.statements[0]

    assert expr_stmt.token.type == token.INT
    assert expr_stmt.token_literal() == '1234'

def test_parse_prefix_expression():
    program_in = '!5; -15;'
    l = Lexer(program_in)
    p = Parser(l)

    program = p.parse_program()
    assert program != None
    assert len(program.statements) == 2;
    
    expected = [(token.BANG, '!', 5), (token.MINUS, '-', 15)]
    for i, stmt in enumerate(program.statements):
        expr = stmt.expression # prefix expr
        expect = expected[i]
        assert expr.token.type == expect[0]
        assert expr.op == expect[1]
        assert expr.expression.value == expect[2]

def test_parse_infix_expression():
    program_in = '5 + 5;'
    expected_result = (5, '+', 5)

    l = Lexer(program_in)
    p = Parser(l)

    program = p.parse_program()

    assert program != None
    assert len(program.statements) == 1

    expr_stmt = program.statements[0]
    infix_expr = expr_stmt.expression

    assert infix_expr.left_expr.value == expected_result[0]
    assert infix_expr.op == expected_result[1]
    assert infix_expr.right_expr.value == expected_result[2]
