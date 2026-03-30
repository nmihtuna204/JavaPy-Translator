grammar command;

program: command+ EOF;

command: verb noun* target? | non_command;

subject: ID;

non_command: ID+ TO*;

verb: ('show' | 'tell' | 'save' | 'retrieve' | 'get' | 'store'| 'translate'| 'see');
noun: ID;
target: source TO target_lang;

source: PYTHON | JAVA;
target_lang: PYTHON | JAVA;

TO: 'to';
PYTHON: 'python';
JAVA: 'java';

ID: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip;  // Add this to skip whitespace