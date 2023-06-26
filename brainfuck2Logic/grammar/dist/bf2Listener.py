# Generated from bf2.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .bf2Parser import bf2Parser
else:
    from bf2Parser import bf2Parser

# This class defines a complete listener for a parse tree produced by bf2Parser.
class bf2Listener(ParseTreeListener):

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
        pass

    # Exit a parse tree produced by bf2Parser#addSubOperation.
    def exitAddSubOperation(self, ctx:bf2Parser.AddSubOperationContext):
        pass


    # Enter a parse tree produced by bf2Parser#multiDivOperation.
    def enterMultiDivOperation(self, ctx:bf2Parser.MultiDivOperationContext):
        pass

    # Exit a parse tree produced by bf2Parser#multiDivOperation.
    def exitMultiDivOperation(self, ctx:bf2Parser.MultiDivOperationContext):
        pass


    # Enter a parse tree produced by bf2Parser#pointerOperation.
    def enterPointerOperation(self, ctx:bf2Parser.PointerOperationContext):
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
        pass

    # Exit a parse tree produced by bf2Parser#whileLoop.
    def exitWhileLoop(self, ctx:bf2Parser.WhileLoopContext):
        pass


    # Enter a parse tree produced by bf2Parser#forLoop.
    def enterForLoop(self, ctx:bf2Parser.ForLoopContext):
        pass

    # Exit a parse tree produced by bf2Parser#forLoop.
    def exitForLoop(self, ctx:bf2Parser.ForLoopContext):
        pass


    # Enter a parse tree produced by bf2Parser#block.
    def enterBlock(self, ctx:bf2Parser.BlockContext):
        pass

    # Exit a parse tree produced by bf2Parser#block.
    def exitBlock(self, ctx:bf2Parser.BlockContext):
        pass


    # Enter a parse tree produced by bf2Parser#decisiveBlock.
    def enterDecisiveBlock(self, ctx:bf2Parser.DecisiveBlockContext):
        pass

    # Exit a parse tree produced by bf2Parser#decisiveBlock.
    def exitDecisiveBlock(self, ctx:bf2Parser.DecisiveBlockContext):
        pass


    # Enter a parse tree produced by bf2Parser#elifBlock.
    def enterElifBlock(self, ctx:bf2Parser.ElifBlockContext):
        pass

    # Exit a parse tree produced by bf2Parser#elifBlock.
    def exitElifBlock(self, ctx:bf2Parser.ElifBlockContext):
        pass


    # Enter a parse tree produced by bf2Parser#elseBlock.
    def enterElseBlock(self, ctx:bf2Parser.ElseBlockContext):
        pass

    # Exit a parse tree produced by bf2Parser#elseBlock.
    def exitElseBlock(self, ctx:bf2Parser.ElseBlockContext):
        pass


    # Enter a parse tree produced by bf2Parser#numberSpecifier.
    def enterNumberSpecifier(self, ctx:bf2Parser.NumberSpecifierContext):
        pass

    # Exit a parse tree produced by bf2Parser#numberSpecifier.
    def exitNumberSpecifier(self, ctx:bf2Parser.NumberSpecifierContext):
        pass


    # Enter a parse tree produced by bf2Parser#finalValueOperation.
    def enterFinalValueOperation(self, ctx:bf2Parser.FinalValueOperationContext):
        pass

    # Exit a parse tree produced by bf2Parser#finalValueOperation.
    def exitFinalValueOperation(self, ctx:bf2Parser.FinalValueOperationContext):
        pass


    # Enter a parse tree produced by bf2Parser#finalPointerOperation.
    def enterFinalPointerOperation(self, ctx:bf2Parser.FinalPointerOperationContext):
        pass

    # Exit a parse tree produced by bf2Parser#finalPointerOperation.
    def exitFinalPointerOperation(self, ctx:bf2Parser.FinalPointerOperationContext):
        pass


    # Enter a parse tree produced by bf2Parser#readOperation.
    def enterReadOperation(self, ctx:bf2Parser.ReadOperationContext):
        pass

    # Exit a parse tree produced by bf2Parser#readOperation.
    def exitReadOperation(self, ctx:bf2Parser.ReadOperationContext):
        pass


    # Enter a parse tree produced by bf2Parser#writeOperation.
    def enterWriteOperation(self, ctx:bf2Parser.WriteOperationContext):
        pass

    # Exit a parse tree produced by bf2Parser#writeOperation.
    def exitWriteOperation(self, ctx:bf2Parser.WriteOperationContext):
        pass



del bf2Parser