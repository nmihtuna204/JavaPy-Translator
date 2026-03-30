# Generated from proj.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .projParser import projParser
else:
    from projParser import projParser

# This class defines a complete generic visitor for a parse tree produced by projParser.

class projVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by projParser#program.
    def visitProgram(self, ctx:projParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by projParser#stmt.
    def visitStmt(self, ctx:projParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by projParser#whileStmt.
    def visitWhileStmt(self, ctx:projParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by projParser#forStmt.
    def visitForStmt(self, ctx:projParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by projParser#rangeExp.
    def visitRangeExp(self, ctx:projParser.RangeExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by projParser#asg.
    def visitAsg(self, ctx:projParser.AsgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by projParser#ifStmt.
    def visitIfStmt(self, ctx:projParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by projParser#elifStmt.
    def visitElifStmt(self, ctx:projParser.ElifStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by projParser#elseStmt.
    def visitElseStmt(self, ctx:projParser.ElseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by projParser#funcStmt.
    def visitFuncStmt(self, ctx:projParser.FuncStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by projParser#breakStmt.
    def visitBreakStmt(self, ctx:projParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by projParser#postfixStmt.
    def visitPostfixStmt(self, ctx:projParser.PostfixStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by projParser#returnStmt.
    def visitReturnStmt(self, ctx:projParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by projParser#mainStmt.
    def visitMainStmt(self, ctx:projParser.MainStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by projParser#printStmt.
    def visitPrintStmt(self, ctx:projParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by projParser#block.
    def visitBlock(self, ctx:projParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by projParser#callStmt.
    def visitCallStmt(self, ctx:projParser.CallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by projParser#questStmt.
    def visitQuestStmt(self, ctx:projParser.QuestStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by projParser#exp.
    def visitExp(self, ctx:projParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by projParser#logicExp.
    def visitLogicExp(self, ctx:projParser.LogicExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by projParser#compExp.
    def visitCompExp(self, ctx:projParser.CompExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by projParser#addExp.
    def visitAddExp(self, ctx:projParser.AddExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by projParser#mulExp.
    def visitMulExp(self, ctx:projParser.MulExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by projParser#unaryExp.
    def visitUnaryExp(self, ctx:projParser.UnaryExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by projParser#verb.
    def visitVerb(self, ctx:projParser.VerbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by projParser#noun.
    def visitNoun(self, ctx:projParser.NounContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by projParser#atom.
    def visitAtom(self, ctx:projParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by projParser#postfix.
    def visitPostfix(self, ctx:projParser.PostfixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by projParser#printArgs.
    def visitPrintArgs(self, ctx:projParser.PrintArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by projParser#param.
    def visitParam(self, ctx:projParser.ParamContext):
        return self.visitChildren(ctx)



del projParser