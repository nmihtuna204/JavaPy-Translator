# Generated from py2java.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .py2javaParser import py2javaParser
else:
    from py2javaParser import py2javaParser

# This class defines a complete generic visitor for a parse tree produced by py2javaParser.

class py2javaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by py2javaParser#program.
    def visitProgram(self, ctx:py2javaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by py2javaParser#stmt.
    def visitStmt(self, ctx:py2javaParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by py2javaParser#whileStmt.
    def visitWhileStmt(self, ctx:py2javaParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by py2javaParser#forStmt.
    def visitForStmt(self, ctx:py2javaParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by py2javaParser#rangeExp.
    def visitRangeExp(self, ctx:py2javaParser.RangeExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by py2javaParser#asg.
    def visitAsg(self, ctx:py2javaParser.AsgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by py2javaParser#ifStmt.
    def visitIfStmt(self, ctx:py2javaParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by py2javaParser#elifStmt.
    def visitElifStmt(self, ctx:py2javaParser.ElifStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by py2javaParser#elseStmt.
    def visitElseStmt(self, ctx:py2javaParser.ElseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by py2javaParser#funcStmt.
    def visitFuncStmt(self, ctx:py2javaParser.FuncStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by py2javaParser#breakStmt.
    def visitBreakStmt(self, ctx:py2javaParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by py2javaParser#postfixStmt.
    def visitPostfixStmt(self, ctx:py2javaParser.PostfixStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by py2javaParser#returnStmt.
    def visitReturnStmt(self, ctx:py2javaParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by py2javaParser#mainStmt.
    def visitMainStmt(self, ctx:py2javaParser.MainStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by py2javaParser#printStmt.
    def visitPrintStmt(self, ctx:py2javaParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by py2javaParser#block.
    def visitBlock(self, ctx:py2javaParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by py2javaParser#callStmt.
    def visitCallStmt(self, ctx:py2javaParser.CallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by py2javaParser#exp.
    def visitExp(self, ctx:py2javaParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by py2javaParser#logicExp.
    def visitLogicExp(self, ctx:py2javaParser.LogicExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by py2javaParser#compExp.
    def visitCompExp(self, ctx:py2javaParser.CompExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by py2javaParser#addExp.
    def visitAddExp(self, ctx:py2javaParser.AddExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by py2javaParser#mulExp.
    def visitMulExp(self, ctx:py2javaParser.MulExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by py2javaParser#unaryExp.
    def visitUnaryExp(self, ctx:py2javaParser.UnaryExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by py2javaParser#atom.
    def visitAtom(self, ctx:py2javaParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by py2javaParser#postfix.
    def visitPostfix(self, ctx:py2javaParser.PostfixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by py2javaParser#printArgs.
    def visitPrintArgs(self, ctx:py2javaParser.PrintArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by py2javaParser#param.
    def visitParam(self, ctx:py2javaParser.ParamContext):
        return self.visitChildren(ctx)



del py2javaParser