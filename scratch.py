from monkey.interpreter.lexer import Lexer
from monkey.interpreter.parser import Parser

l = Lexer('!15;-4;')
p = Parser(l)

program = p.parse_program()
for expr_stmt in program.statements:
    print(expr_stmt.token)
