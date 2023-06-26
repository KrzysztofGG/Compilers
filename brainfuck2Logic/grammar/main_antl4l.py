import sys
from antlr4 import *
from dist.bf2Lexer import bf2Lexer
from dist.bf2Parser import bf2Parser
from dist.bf2Listener import bf2Listener
from dist.bf2Visitor import bf2Visitor
from errorListener import ThrowingErrorListener
import os

if __name__ == "__main__":

    try:
        inputStream = InputStream(">(2)+++[+]-(2).<?(3){++--}|(2){+-}:{+}&(7){+-.}*(2)\n")
        lexer = bf2Lexer(inputStream)
        lexer.removeErrorListener(lexer._listeners[0])
        lexer.addErrorListener(ThrowingErrorListener())

        stream = CommonTokenStream(lexer)
        parser = bf2Parser(stream)
        parser.removeErrorListener(parser._listeners[0])
        parser.addErrorListener(ThrowingErrorListener())

        context = parser.program()
        listener = bf2Listener()
        visitor = bf2Visitor()
        visitor.visit(context)

        visitor.generateFile("output.c")
    except Exception as e:
        print(e)
    

        
        