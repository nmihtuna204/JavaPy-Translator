# Generated from command.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("j\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\7\r_\n\r\f\r\16\rb\13\r\3\16\6\16e\n\16\r\16\16\16")
        buf.write("f\3\16\3\16\2\2\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\3\2\5\5\2C\\aac|\6\2\62;")
        buf.write("C\\aac|\5\2\13\f\17\17\"\"\2k\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5\"\3\2")
        buf.write("\2\2\7\'\3\2\2\2\t,\3\2\2\2\13\65\3\2\2\2\r9\3\2\2\2\17")
        buf.write("?\3\2\2\2\21I\3\2\2\2\23M\3\2\2\2\25P\3\2\2\2\27W\3\2")
        buf.write("\2\2\31\\\3\2\2\2\33d\3\2\2\2\35\36\7u\2\2\36\37\7j\2")
        buf.write("\2\37 \7q\2\2 !\7y\2\2!\4\3\2\2\2\"#\7v\2\2#$\7g\2\2$")
        buf.write("%\7n\2\2%&\7n\2\2&\6\3\2\2\2\'(\7u\2\2()\7c\2\2)*\7x\2")
        buf.write("\2*+\7g\2\2+\b\3\2\2\2,-\7t\2\2-.\7g\2\2./\7v\2\2/\60")
        buf.write("\7t\2\2\60\61\7k\2\2\61\62\7g\2\2\62\63\7x\2\2\63\64\7")
        buf.write("g\2\2\64\n\3\2\2\2\65\66\7i\2\2\66\67\7g\2\2\678\7v\2")
        buf.write("\28\f\3\2\2\29:\7u\2\2:;\7v\2\2;<\7q\2\2<=\7t\2\2=>\7")
        buf.write("g\2\2>\16\3\2\2\2?@\7v\2\2@A\7t\2\2AB\7c\2\2BC\7p\2\2")
        buf.write("CD\7u\2\2DE\7n\2\2EF\7c\2\2FG\7v\2\2GH\7g\2\2H\20\3\2")
        buf.write("\2\2IJ\7u\2\2JK\7g\2\2KL\7g\2\2L\22\3\2\2\2MN\7v\2\2N")
        buf.write("O\7q\2\2O\24\3\2\2\2PQ\7r\2\2QR\7{\2\2RS\7v\2\2ST\7j\2")
        buf.write("\2TU\7q\2\2UV\7p\2\2V\26\3\2\2\2WX\7l\2\2XY\7c\2\2YZ\7")
        buf.write("x\2\2Z[\7c\2\2[\30\3\2\2\2\\`\t\2\2\2]_\t\3\2\2^]\3\2")
        buf.write("\2\2_b\3\2\2\2`^\3\2\2\2`a\3\2\2\2a\32\3\2\2\2b`\3\2\2")
        buf.write("\2ce\t\4\2\2dc\3\2\2\2ef\3\2\2\2fd\3\2\2\2fg\3\2\2\2g")
        buf.write("h\3\2\2\2hi\b\16\2\2i\34\3\2\2\2\5\2`f\3\b\2\2")
        return buf.getvalue()


class commandLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    TO = 9
    PYTHON = 10
    JAVA = 11
    ID = 12
    WS = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'show'", "'tell'", "'save'", "'retrieve'", "'get'", "'store'", 
            "'translate'", "'see'", "'to'", "'python'", "'java'" ]

    symbolicNames = [ "<INVALID>",
            "TO", "PYTHON", "JAVA", "ID", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "TO", "PYTHON", "JAVA", "ID", "WS" ]

    grammarFileName = "command.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


