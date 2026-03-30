# Generated from java2py.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .java2pyParser import java2pyParser
else:
    from java2pyParser import java2pyParser

# This class defines a complete generic visitor for a parse tree produced by java2pyParser.

class java2pyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by java2pyParser#program.
    def visitProgram(self, ctx:java2pyParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java2pyParser#classDef.
    def visitClassDef(self, ctx:java2pyParser.ClassDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java2pyParser#classBody.
    def visitClassBody(self, ctx:java2pyParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java2pyParser#methodDef.
    def visitMethodDef(self, ctx:java2pyParser.MethodDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java2pyParser#stmt.
    def visitStmt(self, ctx:java2pyParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java2pyParser#whileStmt.
    def visitWhileStmt(self, ctx:java2pyParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java2pyParser#forStmt.
    def visitForStmt(self, ctx:java2pyParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java2pyParser#asg.
    def visitAsg(self, ctx:java2pyParser.AsgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java2pyParser#ifStmt.
    def visitIfStmt(self, ctx:java2pyParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java2pyParser#elifStmt.
    def visitElifStmt(self, ctx:java2pyParser.ElifStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java2pyParser#elseStmt.
    def visitElseStmt(self, ctx:java2pyParser.ElseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java2pyParser#funcStmt.
    def visitFuncStmt(self, ctx:java2pyParser.FuncStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java2pyParser#breakStmt.
    def visitBreakStmt(self, ctx:java2pyParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java2pyParser#postfixStmt.
    def visitPostfixStmt(self, ctx:java2pyParser.PostfixStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java2pyParser#returnStmt.
    def visitReturnStmt(self, ctx:java2pyParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java2pyParser#printStmt.
    def visitPrintStmt(self, ctx:java2pyParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java2pyParser#block.
    def visitBlock(self, ctx:java2pyParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java2pyParser#callStmt.
    def visitCallStmt(self, ctx:java2pyParser.CallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java2pyParser#exp.
    def visitExp(self, ctx:java2pyParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java2pyParser#logicExp.
    def visitLogicExp(self, ctx:java2pyParser.LogicExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java2pyParser#compExp.
    def visitCompExp(self, ctx:java2pyParser.CompExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java2pyParser#addExp.
    def visitAddExp(self, ctx:java2pyParser.AddExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java2pyParser#mulExp.
    def visitMulExp(self, ctx:java2pyParser.MulExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java2pyParser#unaryExp.
    def visitUnaryExp(self, ctx:java2pyParser.UnaryExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java2pyParser#atom.
    def visitAtom(self, ctx:java2pyParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java2pyParser#postfix.
    def visitPostfix(self, ctx:java2pyParser.PostfixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java2pyParser#printArgs.
    def visitPrintArgs(self, ctx:java2pyParser.PrintArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java2pyParser#param.
    def visitParam(self, ctx:java2pyParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by java2pyParser#javaType.
    def visitJavaType(self, ctx:java2pyParser.JavaTypeContext):
        return self.visitChildren(ctx)



del java2pyParser