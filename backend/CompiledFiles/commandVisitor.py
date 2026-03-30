# Generated from command.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .commandParser import commandParser
else:
    from commandParser import commandParser

# This class defines a complete generic visitor for a parse tree produced by commandParser.

class commandVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by commandParser#program.
    def visitProgram(self, ctx:commandParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by commandParser#command.
    def visitCommand(self, ctx:commandParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by commandParser#subject.
    def visitSubject(self, ctx:commandParser.SubjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by commandParser#non_command.
    def visitNon_command(self, ctx:commandParser.Non_commandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by commandParser#verb.
    def visitVerb(self, ctx:commandParser.VerbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by commandParser#noun.
    def visitNoun(self, ctx:commandParser.NounContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by commandParser#target.
    def visitTarget(self, ctx:commandParser.TargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by commandParser#source.
    def visitSource(self, ctx:commandParser.SourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by commandParser#target_lang.
    def visitTarget_lang(self, ctx:commandParser.Target_langContext):
        return self.visitChildren(ctx)



del commandParser