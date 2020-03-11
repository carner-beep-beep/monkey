from monkey.interpreter.lexer import Lexer
from monkey.interpreter.parser import Parser

l = Lexer('foobar;')
p = Parser(l)

program = p.parse_program()
expr_stmt = program.statements[0]
print(f'expr_stmt token: {expr_stmt.token} expression: {expr_stmt.expression}')
