grammar java2py;

// Grammar rules
program: classDef EOF;

classDef: PUBLIC CLASS ID '{' classBody '}';

classBody: (methodDef)*;

methodDef: PUBLIC STATIC javaType ID '(' param? ')' block;

stmt: whileStmt
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

whileStmt: WHILE '(' exp ')' block;

forStmt: FOR '(' javaType ID '=' exp ';' exp ';' postfixStmt ')' block;

asg: javaType? ID '=' exp ';';

ifStmt: IF '(' exp ')' block (elifStmt)* elseStmt?;

elifStmt: ELSE IF '(' exp ')' block;

elseStmt: ELSE block;

funcStmt: PUBLIC STATIC javaType ID '(' param? ')' block;

breakStmt: BREAK ';';

postfixStmt: ID op=('++'|'--'|'+='|'-=') exp? ';';

returnStmt: RETURN exp ';';

printStmt: SYSTEM '.' OUT '.' PRINTLN '(' printArgs? ')' ';';

block: '{' stmt* '}';

callStmt: ID '(' exp? ')' ';';

// Expression hierarchy with logical operators
exp: logicExp;

logicExp: compExp
        | logicExp op=('&&'|'||') compExp;

compExp: addExp
       | compExp op=('>'|'<'|'=='|'!='|'<='|'>=') addExp;

addExp: mulExp
      | addExp op=('+'|'-') mulExp;

mulExp: unaryExp
      | mulExp op=('*'|'/') unaryExp;

unaryExp: op=('!'|'-') unaryExp
        | atom;

atom: NUMBER
    | FLOAT
    | TRUE
    | FALSE
    | NULL
    | ID '(' (exp (',' exp)*)? ')'
    | ID postfix
    | ID
    | '(' exp ')'
    | STRING
    ;

postfix: op=('++'|'--'|'+='|'-=');

printArgs: exp (',' exp)*;

param: javaType ('[' ']')* ID (',' javaType ('[' ']')* ID)*;

// Types
javaType: INT | DOUBLE | BOOLEAN | STRING | VOID;

// Tokens
PUBLIC: 'public';
CLASS: 'class';
STATIC: 'static';
VOID: 'void';
INT: 'int';
DOUBLE: 'double';
BOOLEAN: 'boolean';
STRING: 'String';
IF: 'if';
ELSE: 'else';
COLON: ':';
BREAK: 'break';
WHILE: 'while';
FOR: 'for';
RETURN: 'return';
SYSTEM: 'System';
OUT: 'out';
PRINTLN: 'println';
TRUE: 'true';
FALSE: 'false';
NULL: 'null';

// Literals and identifiers
STRING_LITERAL: '"' ( ~["\\\r\n] | '\\' . )* '"' 
              | '\'' ( ~['\\\r\n] | '\\' . )* '\'';

ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;

// Whitespace and newlines
NL: ('\r'? '\n' [ \t]*) -> skip;
WS: [ \t]+ -> skip;