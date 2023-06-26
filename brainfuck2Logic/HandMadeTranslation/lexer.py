import ply.lex as lex
import ply.yacc as yacc
import os
# Lex
class MyLexer(object):

    tokens=(
        'MOVE_RIGHT',
        'MOVE_LEFT',
        'ADD_1',
        'MINUS_1',
        'SHOW',
        'EXTRACT',
        'WHILE_BEGIN',
        'WHILE_END',
        'MULTIPLY',
        'DIVIDE',
        'NUMBER',
        'FOR_LOOP',
        'IF',
        'ELIF',
        'ELSE',
        'LPAREN',
        'RPAREN',
        'LBRACKET',
        'RBRACKET',
    )

    t_MOVE_RIGHT= r'>'
    t_MOVE_LEFT = r'<'
    t_ADD_1 = r'\+'
    t_MINUS_1= r'-'
    t_SHOW = r'\.'
    t_EXTRACT = r','
    t_WHILE_BEGIN =r'\['
    t_WHILE_END = r'\]'
    t_MULTIPLY = r'\*'
    t_DIVIDE = r'\/'
    t_FOR_LOOP = r'\&'
    t_IF = r'\?'
    t_ELIF = r'\|'
    t_ELSE = r'\:'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LBRACKET = r'\{'
    t_RBRACKET = r'\}'
    t_ignore = '  \t'

#Yacc
    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(self, t) :
        print("Illegal character '%s'" %t.value[0])
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def get_tokens(self, input_file):
        f = open(input_file, "r")
        self.lexer.input(f.read())
        tokens = [(token.type, token.value) for token in self.lexer]
        return tokens
    
    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)
    
    def test_file(self, file):
        f = open(file, "r")
        self.lexer.input(f.read())
        for token in self.lexer:
            print(f"{token.type}({token.value})")

# m = MyLexer()
# m.build()
# m.test_file(os.path.join(os.getcwd(), "grammar", "test.txt"))

