# Generated from proj.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .projParser import projParser
else:
    from projParser import projParser

# This class defines a complete listener for a parse tree produced by projParser.
class projListener(ParseTreeListener):

    # Enter a parse tree produced by projParser#program.
    def enterProgram(self, ctx:projParser.ProgramContext):
        pass

    # Exit a parse tree produced by projParser#program.
    def exitProgram(self, ctx:projParser.ProgramContext):
        pass


    # Enter a parse tree produced by projParser#stm.
    def enterStm(self, ctx:projParser.StmContext):
        pass

    # Exit a parse tree produced by projParser#stm.
    def exitStm(self, ctx:projParser.StmContext):
        pass


    # Enter a parse tree produced by projParser#asg.
    def enterAsg(self, ctx:projParser.AsgContext):
        pass

    # Exit a parse tree produced by projParser#asg.
    def exitAsg(self, ctx:projParser.AsgContext):
        pass


    # Enter a parse tree produced by projParser#var.
    def enterVar(self, ctx:projParser.VarContext):
        pass

    # Exit a parse tree produced by projParser#var.
    def exitVar(self, ctx:projParser.VarContext):
        pass


    # Enter a parse tree produced by projParser#exp.
    def enterExp(self, ctx:projParser.ExpContext):
        pass

    # Exit a parse tree produced by projParser#exp.
    def exitExp(self, ctx:projParser.ExpContext):
        pass



del projParser