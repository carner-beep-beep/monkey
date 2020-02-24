from monkey.interpreter.lexer import Lexer
from monkey.interpreter import token

PROMPT = '>> '

def main():
    print('Welcome to the monkey repl!')
    done = False
    while not done:
        i = input(PROMPT)
        if i == 'exit':
            done = True
        else:
            l = Lexer(i)
            tok = l.next_token()
            while tok.type != token.EOF:
                print(tok)
                tok = l.next_token()

if __name__ == '__main__':
    main()
