import ply.lex as lex
import ply.yacc as yacc

# Lex

tokens=(
    'MOVE_RIGHT',
    'MOVE_LEFT',
    'ADD_1',
    'MINUS_1',
    'SHOW',
    'EXTRACT',
    'WHILE_BEGIN',
    'WHILE_END'
)

t_MOVE_RIGHT= r'>'
t_MOVE_LEFT = r'<'
t_ADD_1 = r'\+'
t_MINUS_1= r'-'
t_SHOW = r'\.'
t_EXTRACT = r','
t_WHILE_BEGIN =r'\['
t_WHILE_END = r'\]'
t_ignore = '  \t'

#Yacc
def t_newline(t):
    r'\n+'
def t_error(t) :
    print("Illegal character '%s'" %t.value[0])
    t.lexer.skip(1)
lexer = lex.lex()
f = open("test.txt","r")
lexer.input( f.read() )
#def func(token):

for token in lexer:
    #func(token)
    print(" %s(%s)" %( token.type, token.value))