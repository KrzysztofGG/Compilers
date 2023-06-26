# Generated from bf2.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .bf2Parser import bf2Parser
else:
    from bf2Parser import bf2Parser

# This class defines a complete generic visitor for a parse tree produced by bf2Parser.

class bf2Visitor(ParseTreeVisitor):


    def __init__(self):
        self.code = ""
        self.for_depth = 0
        self.indent = 1
        self.indexes = ['i', 'j', 'k', 'l', 'm', 'n']

    # Visit a parse tree produced by bf2Parser#program.
    def visitProgram(self, ctx:bf2Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by bf2Parser#instruction.
    def visitInstruction(self, ctx:bf2Parser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by bf2Parser#valueOperation.
    def visitValueOperation(self, ctx:bf2Parser.ValueOperationContext):
        
        line = self.indent*"\t"
        line += f"*ptr {ctx.getText()[0]}="

        if len(ctx.getText()) > 1:
            line += f" {ctx.getText()[-2]};\n"
        else:
            line += " 1;\n"
        self.code += line 
        return self.visitChildren(ctx)


    # Visit a parse tree produced by bf2Parser#addSubOperation.
    def visitAddSubOperation(self, ctx:bf2Parser.AddSubOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by bf2Parser#multiDivOperation.
    def visitMultiDivOperation(self, ctx:bf2Parser.MultiDivOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by bf2Parser#pointerOperation.
    def visitPointerOperation(self, ctx:bf2Parser.PointerOperationContext):
    
        operator = ""
        if ctx.getText()[0] == '>':
            operator = "+"
        elif ctx.getText()[0] == '<':
            operator = "-"

        line = self.indent*"\t"
        line += f"ptr {operator}="
        if len(ctx.getText()) > 1:
            line += f" {ctx.getText()[-2]};\n"
        else:
            line += " 1;\n"

        self.code += line

        return self.visitChildren(ctx)


    # Visit a parse tree produced by bf2Parser#loop.
    def visitLoop(self, ctx:bf2Parser.LoopContext):
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by bf2Parser#whileLoop.
    def visitWhileLoop(self, ctx:bf2Parser.WhileLoopContext):
        
        line = self.indent*"\t"
        line += "while(*ptr){\n"
        self.indent += 1
        self.code += line

        self.visitChildren(ctx)

        self.indent -= 1
        line = self.indent*"\t"
        line += "}\n"
        self.code += line
        return 
    



    # Visit a parse tree produced by bf2Parser#forLoop.
    def visitForLoop(self, ctx:bf2Parser.ForLoopContext):
        
        index = self.indexes[self.for_depth]

        line = self.indent*"\t"
        line += f"for(int {index}=0; {index}<{ctx.getText()[2]}; ++{index})"
        self.for_depth += 1
        self.code += line

        self.visitChildren(ctx)
        
        self.for_depth -= 1

        return 


    # Visit a parse tree produced by bf2Parser#block.
    def visitBlock(self, ctx:bf2Parser.BlockContext):

        line = self.indent*"\t"
        line += ctx.getText()[0] + "\n"
        self.code += line
        self.indent += 1

        self.visitChildren(ctx)

        self.indent -= 1
        line = self.indent*"\t"
        line += ctx.getText()[-1] + "\n"
        self.code += line
        return 


    # Visit a parse tree produced by bf2Parser#decisiveBlock.
    def visitDecisiveBlock(self, ctx:bf2Parser.DecisiveBlockContext):
        
        line = self.indent*"\t"
        line += f"if(*ptr == {ctx.getText()[2]})"
        self.code += line

        return self.visitChildren(ctx)


    # Visit a parse tree produced by bf2Parser#elifBlock.
    def visitElifBlock(self, ctx:bf2Parser.ElifBlockContext):

        line = self.indent*"\t"
        line += f"else if(*ptr == {ctx.getText()[2]})"
        self.code += line

        return self.visitChildren(ctx)


    # Visit a parse tree produced by bf2Parser#elseBlock.
    def visitElseBlock(self, ctx:bf2Parser.ElseBlockContext):
        
        line = self.indent*"\t"
        line += "else"
        self.code += line
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by bf2Parser#numberSpecifier.
    def visitNumberSpecifier(self, ctx:bf2Parser.NumberSpecifierContext):
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by bf2Parser#finalValueOperation.
    def visitFinalValueOperation(self, ctx:bf2Parser.FinalValueOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by bf2Parser#finalPointerOperation.
    def visitFinalPointerOperation(self, ctx:bf2Parser.FinalPointerOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by bf2Parser#readOperation.
    def visitReadOperation(self, ctx:bf2Parser.ReadOperationContext):
        
        line = self.indent*"\t"
        line += "*ptr = getchar();\n"
        self.code += line
        return self.visitChildren(ctx)


    # Visit a parse tree produced by bf2Parser#writeOperation.
    def visitWriteOperation(self, ctx:bf2Parser.WriteOperationContext):
        
        line = self.indent*"\t"
        line += "putchar(*ptr);\n"
        self.code += line
        return self.visitChildren(ctx)

    def generateFile(self, output_file):
        prefix = "#include \"stdio.h\"\n\nint main(){\n\tchar tape[20000] = {0};\n\tchar *ptr = tape;\n"
        data = prefix + self.code + "\n\treturn 0;\n}"
        with open(output_file, "w") as f:
            f.write(data)

del bf2Parser