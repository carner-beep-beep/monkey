from monkey.interpreter import lexer

def test_lexer():
    l = lexer.Lexer('+=(){}')
