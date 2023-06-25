# Generated from bf2.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .bf2Parser import bf2Parser
else:
    from bf2Parser import bf2Parser

# This class defines a complete listener for a parse tree produced by bf2Parser.
class bf2Listener(ParseTreeListener):

    def __init__(self):
        self.command = ""
        self.code = ""
        self.specifier_present = False
        self.is_for = False
        self.is_if = False
        self.is_elif = False
        

    # Enter a parse tree produced by bf2Parser#program.
    def enterProgram(self, ctx:bf2Parser.ProgramContext):
        pass

    # Exit a parse tree produced by bf2Parser#program.
    def exitProgram(self, ctx:bf2Parser.ProgramContext):
        pass


    # Enter a parse tree produced by bf2Parser#instruction.
    def enterInstruction(self, ctx:bf2Parser.InstructionContext):
        pass

    # Exit a parse tree produced by bf2Parser#instruction.
    def exitInstruction(self, ctx:bf2Parser.InstructionContext):
        pass


    # Enter a parse tree produced by bf2Parser#valueOperation.
    def enterValueOperation(self, ctx:bf2Parser.ValueOperationContext):
        pass

    # Exit a parse tree produced by bf2Parser#valueOperation.
    def exitValueOperation(self, ctx:bf2Parser.ValueOperationContext):
        pass


    # Enter a parse tree produced by bf2Parser#addSubOperation.
    def enterAddSubOperation(self, ctx:bf2Parser.AddSubOperationContext):

        if ctx.getChildCount() > 1:
            self.specifier_present = True
        pass

    # Exit a parse tree produced by bf2Parser#addSubOperation.
    def exitAddSubOperation(self, ctx:bf2Parser.AddSubOperationContext):
        pass


    # Enter a parse tree produced by bf2Parser#multiDivOperation.
    def enterMultiDivOperation(self, ctx:bf2Parser.MultiDivOperationContext):

        self.specifier_present = True
        pass

    # Exit a parse tree produced by bf2Parser#multiDivOperation.
    def exitMultiDivOperation(self, ctx:bf2Parser.MultiDivOperationContext):
        pass


    # Enter a parse tree produced by bf2Parser#pointerOperation.
    def enterPointerOperation(self, ctx:bf2Parser.PointerOperationContext):

        if ctx.getChildCount() > 1:
            self.specifier_present = True
        pass

    # Exit a parse tree produced by bf2Parser#pointerOperation.
    def exitPointerOperation(self, ctx:bf2Parser.PointerOperationContext):
        pass


    # Enter a parse tree produced by bf2Parser#loop.
    def enterLoop(self, ctx:bf2Parser.LoopContext):
        pass

    # Exit a parse tree produced by bf2Parser#loop.
    def exitLoop(self, ctx:bf2Parser.LoopContext):
        pass


    # Enter a parse tree produced by bf2Parser#whileLoop.
    def enterWhileLoop(self, ctx:bf2Parser.WhileLoopContext):

        self.code += "while(*ptr){\n"
        pass

    # Exit a parse tree produced by bf2Parser#whileLoop.
    def exitWhileLoop(self, ctx:bf2Parser.WhileLoopContext):

        self.code += "}\n"
        pass


    # Enter a parse tree produced by bf2Parser#forLoop.
    def enterForLoop(self, ctx:bf2Parser.ForLoopContext):

        self.is_for = True
        pass

    # Exit a parse tree produced by bf2Parser#forLoop.
    def exitForLoop(self, ctx:bf2Parser.ForLoopContext):
        pass


    # Enter a parse tree produced by bf2Parser#block.
    def enterBlock(self, ctx:bf2Parser.BlockContext):

        self.code += "{\n"
        pass

    # Exit a parse tree produced by bf2Parser#block.
    def exitBlock(self, ctx:bf2Parser.BlockContext):
        
        self.code += "}\n"
        pass


    # Enter a parse tree produced by bf2Parser#decisiveBlock.
    def enterDecisiveBlock(self, ctx:bf2Parser.DecisiveBlockContext):

        self.is_if = True
        pass

    # Exit a parse tree produced by bf2Parser#decisiveBlock.
    def exitDecisiveBlock(self, ctx:bf2Parser.DecisiveBlockContext):
        pass


    # Enter a parse tree produced by bf2Parser#elifBlock.
    def enterElifBlock(self, ctx:bf2Parser.ElifBlockContext):

        self.is_elif = True
        pass

    # Exit a parse tree produced by bf2Parser#elifBlock.
    def exitElifBlock(self, ctx:bf2Parser.ElifBlockContext):
        pass


    # Enter a parse tree produced by bf2Parser#elseBlock.
    def enterElseBlock(self, ctx:bf2Parser.ElseBlockContext):

        self.code += "else"
        pass

    # Exit a parse tree produced by bf2Parser#elseBlock.
    def exitElseBlock(self, ctx:bf2Parser.ElseBlockContext):
        pass


    # Enter a parse tree produced by bf2Parser#numberSpecifier.
    def enterNumberSpecifier(self, ctx:bf2Parser.NumberSpecifierContext):

        if self.command != "":
            line = self.command + ctx.PositiveNumber() + ";\n"
            self.command = ""
        if self.is_for:
            line = "for(int i=0; i<{num}; ++i)".format(num=ctx.PositiveNumber())
        elif self.is_if:
            line = "if(*ptr == {num})".format(num=ctx.PositiveNumber())
        elif self.is_elif:
            line = "else if(*ptr == {num})".format(num=ctx.PositiveNumber())

        self.code += line

        # pass

    # Exit a parse tree produced by bf2Parser#numberSpecifier.
    def exitNumberSpecifier(self, ctx:bf2Parser.NumberSpecifierContext):
        pass


    # Enter a parse tree produced by bf2Parser#finalValueOperation.
    def enterFinalValueOperation(self, ctx:bf2Parser.FinalValueOperationContext):

        if self.specifier_present:
            self.command = f"*ptr {ctx.getText()}= "
            self.specifier_present = False
        else:
            self.code += f"*ptr {ctx.getText()}= 1;\n"
        pass

    # Exit a parse tree produced by bf2Parser#finalValueOperation.
    def exitFinalValueOperation(self, ctx:bf2Parser.FinalValueOperationContext):

        pass


    # Enter a parse tree produced by bf2Parser#finalPointerOperation.
    def enterFinalPointerOperation(self, ctx:bf2Parser.FinalPointerOperationContext):

        operation = ""
        if ctx.getText() == "<":
            operation = "-"
        elif ctx.getText() == ">":
            operation = "+"

        if self.specifier_present:
            self.command = f"ptr {operation}= "
            self.specifier_present = False
        else:
            self.code += f"ptr {operation}= 1;\n"
        pass

    # Exit a parse tree produced by bf2Parser#finalPointerOperation.
    def exitFinalPointerOperation(self, ctx:bf2Parser.FinalPointerOperationContext):
        pass


    # Enter a parse tree produced by bf2Parser#readOperation.
    def enterReadOperation(self, ctx:bf2Parser.ReadOperationContext):

        self.code += "*ptr = getchar();\n"
        pass

    # Exit a parse tree produced by bf2Parser#readOperation.
    def exitReadOperation(self, ctx:bf2Parser.ReadOperationContext):
        pass


    # Enter a parse tree produced by bf2Parser#writeOperation.
    def enterWriteOperation(self, ctx:bf2Parser.WriteOperationContext):

        self.code += "putchar(*ptr);\n"
        pass

    # Exit a parse tree produced by bf2Parser#writeOperation.
    def exitWriteOperation(self, ctx:bf2Parser.WriteOperationContext):
        pass

    def generateFile(self, output_file):
        prefix = "#include \"stdio.h\"\n\nint main(){\n\tchar tape[20000] = {0};\n\tchar *ptr = tape;\n"
        data = prefix + self.code + "\n\treturn 0;\n}"
        with open(output_file, "w") as f:
            f.write(data)



del bf2Parser



