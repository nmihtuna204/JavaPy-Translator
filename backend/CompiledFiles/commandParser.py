# Generated from command.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("B\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\6\2\26\n\2\r\2\16\2\27\3\2\3")
        buf.write("\2\3\3\3\3\7\3\36\n\3\f\3\16\3!\13\3\3\3\5\3$\n\3\3\3")
        buf.write("\5\3\'\n\3\3\4\3\4\3\5\6\5,\n\5\r\5\16\5-\3\5\7\5\61\n")
        buf.write("\5\f\5\16\5\64\13\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\n\3\n\3\n\2\2\13\2\4\6\b\n\f\16\20\22\2\4\3\2")
        buf.write("\3\n\3\2\f\r\2>\2\25\3\2\2\2\4&\3\2\2\2\6(\3\2\2\2\b+")
        buf.write("\3\2\2\2\n\65\3\2\2\2\f\67\3\2\2\2\169\3\2\2\2\20=\3\2")
        buf.write("\2\2\22?\3\2\2\2\24\26\5\4\3\2\25\24\3\2\2\2\26\27\3\2")
        buf.write("\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\31\3\2\2\2\31\32\7")
        buf.write("\2\2\3\32\3\3\2\2\2\33\37\5\n\6\2\34\36\5\f\7\2\35\34")
        buf.write("\3\2\2\2\36!\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 #\3\2\2")
        buf.write("\2!\37\3\2\2\2\"$\5\16\b\2#\"\3\2\2\2#$\3\2\2\2$\'\3\2")
        buf.write("\2\2%\'\5\b\5\2&\33\3\2\2\2&%\3\2\2\2\'\5\3\2\2\2()\7")
        buf.write("\16\2\2)\7\3\2\2\2*,\7\16\2\2+*\3\2\2\2,-\3\2\2\2-+\3")
        buf.write("\2\2\2-.\3\2\2\2.\62\3\2\2\2/\61\7\13\2\2\60/\3\2\2\2")
        buf.write("\61\64\3\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63\t\3\2\2")
        buf.write("\2\64\62\3\2\2\2\65\66\t\2\2\2\66\13\3\2\2\2\678\7\16")
        buf.write("\2\28\r\3\2\2\29:\5\20\t\2:;\7\13\2\2;<\5\22\n\2<\17\3")
        buf.write("\2\2\2=>\t\3\2\2>\21\3\2\2\2?@\t\3\2\2@\23\3\2\2\2\b\27")
        buf.write("\37#&-\62")
        return buf.getvalue()


class commandParser ( Parser ):

    grammarFileName = "command.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'show'", "'tell'", "'save'", "'retrieve'", 
                     "'get'", "'store'", "'translate'", "'see'", "'to'", 
                     "'python'", "'java'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "TO", "PYTHON", "JAVA", "ID", "WS" ]

    RULE_program = 0
    RULE_command = 1
    RULE_subject = 2
    RULE_non_command = 3
    RULE_verb = 4
    RULE_noun = 5
    RULE_target = 6
    RULE_source = 7
    RULE_target_lang = 8

    ruleNames =  [ "program", "command", "subject", "non_command", "verb", 
                   "noun", "target", "source", "target_lang" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    TO=9
    PYTHON=10
    JAVA=11
    ID=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(commandParser.EOF, 0)

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(commandParser.CommandContext)
            else:
                return self.getTypedRuleContext(commandParser.CommandContext,i)


        def getRuleIndex(self):
            return commandParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = commandParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.command()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << commandParser.T__0) | (1 << commandParser.T__1) | (1 << commandParser.T__2) | (1 << commandParser.T__3) | (1 << commandParser.T__4) | (1 << commandParser.T__5) | (1 << commandParser.T__6) | (1 << commandParser.T__7) | (1 << commandParser.ID))) != 0)):
                    break

            self.state = 23
            self.match(commandParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def verb(self):
            return self.getTypedRuleContext(commandParser.VerbContext,0)


        def noun(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(commandParser.NounContext)
            else:
                return self.getTypedRuleContext(commandParser.NounContext,i)


        def target(self):
            return self.getTypedRuleContext(commandParser.TargetContext,0)


        def non_command(self):
            return self.getTypedRuleContext(commandParser.Non_commandContext,0)


        def getRuleIndex(self):
            return commandParser.RULE_command

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = commandParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [commandParser.T__0, commandParser.T__1, commandParser.T__2, commandParser.T__3, commandParser.T__4, commandParser.T__5, commandParser.T__6, commandParser.T__7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.verb()
                self.state = 29
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 26
                        self.noun() 
                    self.state = 31
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==commandParser.PYTHON or _la==commandParser.JAVA:
                    self.state = 32
                    self.target()


                pass
            elif token in [commandParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.non_command()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(commandParser.ID, 0)

        def getRuleIndex(self):
            return commandParser.RULE_subject

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubject" ):
                return visitor.visitSubject(self)
            else:
                return visitor.visitChildren(self)




    def subject(self):

        localctx = commandParser.SubjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_subject)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(commandParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Non_commandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(commandParser.ID)
            else:
                return self.getToken(commandParser.ID, i)

        def TO(self, i:int=None):
            if i is None:
                return self.getTokens(commandParser.TO)
            else:
                return self.getToken(commandParser.TO, i)

        def getRuleIndex(self):
            return commandParser.RULE_non_command

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNon_command" ):
                return visitor.visitNon_command(self)
            else:
                return visitor.visitChildren(self)




    def non_command(self):

        localctx = commandParser.Non_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_non_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 40
                    self.match(commandParser.ID)

                else:
                    raise NoViableAltException(self)
                self.state = 43 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==commandParser.TO:
                self.state = 45
                self.match(commandParser.TO)
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VerbContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return commandParser.RULE_verb

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVerb" ):
                return visitor.visitVerb(self)
            else:
                return visitor.visitChildren(self)




    def verb(self):

        localctx = commandParser.VerbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_verb)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << commandParser.T__0) | (1 << commandParser.T__1) | (1 << commandParser.T__2) | (1 << commandParser.T__3) | (1 << commandParser.T__4) | (1 << commandParser.T__5) | (1 << commandParser.T__6) | (1 << commandParser.T__7))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NounContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(commandParser.ID, 0)

        def getRuleIndex(self):
            return commandParser.RULE_noun

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNoun" ):
                return visitor.visitNoun(self)
            else:
                return visitor.visitChildren(self)




    def noun(self):

        localctx = commandParser.NounContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_noun)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(commandParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TargetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def source(self):
            return self.getTypedRuleContext(commandParser.SourceContext,0)


        def TO(self):
            return self.getToken(commandParser.TO, 0)

        def target_lang(self):
            return self.getTypedRuleContext(commandParser.Target_langContext,0)


        def getRuleIndex(self):
            return commandParser.RULE_target

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTarget" ):
                return visitor.visitTarget(self)
            else:
                return visitor.visitChildren(self)




    def target(self):

        localctx = commandParser.TargetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_target)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.source()
            self.state = 56
            self.match(commandParser.TO)
            self.state = 57
            self.target_lang()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SourceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PYTHON(self):
            return self.getToken(commandParser.PYTHON, 0)

        def JAVA(self):
            return self.getToken(commandParser.JAVA, 0)

        def getRuleIndex(self):
            return commandParser.RULE_source

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSource" ):
                return visitor.visitSource(self)
            else:
                return visitor.visitChildren(self)




    def source(self):

        localctx = commandParser.SourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_source)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            _la = self._input.LA(1)
            if not(_la==commandParser.PYTHON or _la==commandParser.JAVA):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Target_langContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PYTHON(self):
            return self.getToken(commandParser.PYTHON, 0)

        def JAVA(self):
            return self.getToken(commandParser.JAVA, 0)

        def getRuleIndex(self):
            return commandParser.RULE_target_lang

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTarget_lang" ):
                return visitor.visitTarget_lang(self)
            else:
                return visitor.visitChildren(self)




    def target_lang(self):

        localctx = commandParser.Target_langContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_target_lang)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            _la = self._input.LA(1)
            if not(_la==commandParser.PYTHON or _la==commandParser.JAVA):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





