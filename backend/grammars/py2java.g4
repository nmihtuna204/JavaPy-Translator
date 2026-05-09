grammar py2java;

// Grammar rules

program: (stmt | NL)+ EOF;

stmt: mainStmt 
    | whileStmt
    | forStmt
    | ifStmt
    | funcStmt
    | asg
    | breakStmt
    | postfixStmt
    | returnStmt
    | printStmt
    | callStmt
    ;

whileStmt: WHILE exp COLON block;

forStmt: FOR ID IN rangeExp COLON block;

rangeExp: RANGE '(' exp (',' exp (',' exp)?)? ')';

asg: ID EQUAL exp NL?;

ifStmt: IF exp COLON block elifStmt* elseStmt?;

elifStmt: ELIF exp COLON block;

elseStmt: ELSE COLON block;

funcStmt: DEF ID '(' param? ')' COLON block;

breakStmt: BREAK NL?;

postfixStmt: ID postfix exp? NL?;

returnStmt: RETURN exp NL?;

mainStmt: IF MAIN COLON block;

printStmt: PRINT '(' printArgs? ')' NL?;

block: NL stmt+;

callStmt: ID '(' exp? ')' NL?;

// Expression hierarchy with logical operators
exp: logicExp;
logicExp: compExp (op=('and'|'or') compExp)*;
compExp: addExp (op=('>'|'<'|'=='|'!='|'<='|'>=') addExp)*;
addExp: mulExp (op=('+'|'-') mulExp)*;
mulExp: unaryExp (op=('*'|'/') unaryExp)*;
unaryExp: op=('not'|'-') unaryExp | atom;

atom: NUMBER
    | FLOAT
    | TRUE
    | FALSE
    | NONE
    | ID '(' (exp (',' exp)*)? ')'
    | ID postfix
    | ID
    | '(' exp ')'
    | STRING
    ;

MAIN: '__name__' WS* '==' WS* ('"__main__"'|'\'__main__\'') ;

postfix: op=('--'|'++'|'+='|'-=');

printArgs: exp (',' exp)*;

param: ID (',' ID)*;

// Tokens

DEF: 'def';
IF: 'if';
ELIF: 'elif';
ELSE: 'else';
COLON: ':';
BREAK: 'break';
WHILE: 'while';
FOR: 'for';
IN: 'in';
RANGE: 'range';
RETURN: 'return';
PRINT: 'print';
TRUE: 'True';
FALSE: 'False';
NONE: 'None';

STRING: '"' ( ~["\\\r\n] | '\\' . )* '"' 
      | '\'' ( ~['\\\r\n] | '\\' . )* '\'' ;
ID: [a-zA-Z_][_a-zA-Z0-9]* ;
EQUAL: '=' ;
NUMBER: [0-9]+ ;
FLOAT: [0-9]+ '.' [0-9]+ ;
NL: ('\r'? '\n' [ \t]*) ;
WS: [ \t]+ -> skip ;