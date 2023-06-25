import sys
from antlr4 import *
from dist.bf2Lexer import bf2Lexer
from dist.bf2Parser import bf2Parser
from dist.bf2Listener import bf2Listener
import os

if __name__ == "__main__":


    input_file = FileStream("test.txt")
    output_file = "ahahhaho_out.c"
    lexer = bf2Lexer(input_file)
    stream = CommonTokenStream(Lexer)
    parser = bf2Parser(stream)
    tree = parser.program()
    listener = bf2Listener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    listener.generateFile(output_file)

    # while True:
    #     file = os.path.join(os.getcwd(), "brainfuck2Logic", "grammar", "test.txt")
    #     output_file = "ahahhaho_out.c"
    #     data = InputStream(input(">>> "))
    #     # with open(file, 'r') as sys.stdin:
    #     #     stream = input()
    #     # stream = 
    #     lexer = bf2Lexer(data)
    #     stream = CommonTokenStream(lexer)

    #     parser = bf2Parser(stream)
    #     context = parser.program()

    #     tree = parser.program()

    #     listener = bf2Listener()
    #     walker = ParseTreeWalker()
    #     walker.walk(listener, tree)
    #     listener.generateFile(output_file)
    #     output = listener.visit(tree)
    #     print(output)
    # except Exception as e:
    #     print(e)

        
        