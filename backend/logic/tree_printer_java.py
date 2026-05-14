from antlr4 import ParserRuleContext, TerminalNode
from CompiledFiles.java2pyLexer import java2pyLexer
from CompiledFiles.java2pyParser import java2pyParser

# Create a direct mapping from token types to names based on java2pyLexer.tokens
TOKEN_TYPE_MAP = {
    1: "LBRACE",
    2: "RBRACE",
    3: "LPAREN",
    4: "RPAREN",
    5: "EQUAL",
    6: "SEMICOLON",
    7: "INC",
    8: "DEC",
    9: "PLUSEQ",
    10: "MINEQ",
    11: "LBRACK",
    12: "RBRACK",
    13: "DOT",
    14: "AND",
    15: "OR",
    16: "GT",
    17: "LT",
    18: "EQ",
    19: "NEQ",
    20: "LTE",
    21: "GTE",
    22: "PLUS",
    23: "MINUS",
    24: "MUL",
    25: "DIV",
    26: "NOT",
    27: "COMMA",
    28: "PUBLIC",
    29: "CLASS",
    30: "STATIC",
    31: "VOID",
    32: "INT",
    33: "DOUBLE",
    34: "BOOLEAN",
    35: "STRING",
    36: "IF",
    37: "ELSE",
    38: "COLON",
    39: "BREAK",
    40: "WHILE",
    41: "FOR",
    42: "RETURN",
    43: "SYSTEM",
    44: "OUT",
    45: "PRINTLN",
    46: "TRUE",
    47: "FALSE",
    48: "NULL",
    49: "MAIN",
    50: "STRING_LITERAL",
    51: "ID",
    52: "NUMBER",
    53: "FLOAT",
    54: "NL",
    55: "WS"
}

def parse_tree_java(tree, indent=0, prefix=""):
    """
    Generate a pretty-printed ANTLR parse tree as a string.
    
    Args:
        tree: The parse tree node (ParserRuleContext or TerminalNode).
        indent: Current indentation level (number of spaces).
        prefix: Prefix for the current line (e.g., for tree branches).
    
    Returns:
        str: The formatted parse tree as a string.
    """
    if tree is None:
        return ""

    # List to collect tree lines
    lines = []
    
    # Indentation string (2 spaces per level)
    indent_str = "  " * indent
    
    if isinstance(tree, TerminalNode):
        # Terminal node (e.g., token like 'count', '=', '1')
        token = tree.getSymbol()
        if token is None:
            return ""
            
        token_type = token.type
        token_text = token.text
        
        # Skip whitespace and newline tokens
        if token_type in [54, 55]:  # NL or WS
            return ""
            
        # Get token name from the map or use a default
        token_name = TOKEN_TYPE_MAP.get(token_type, f"UNKNOWN({token_type})")
            
        lines.append(f"{indent_str}{prefix}Token: {token_text} (type: {token_name})")
    elif isinstance(tree, ParserRuleContext):
        # Rule node (e.g., program, stmt, asg)
        rule_name = java2pyParser.ruleNames[tree.getRuleIndex()]
        lines.append(f"{indent_str}{prefix}Rule: {rule_name}")
        
        # Process children
        children = list(tree.getChildren())
        if not children:
            return f"{indent_str}{prefix}Rule: {rule_name} (empty)"
            
        for i, child in enumerate(children):
            # Determine prefix for child (e.g., ├── for intermediate, └── for last)
            is_last = i == len(children) - 1
            child_prefix = "└── " if is_last else "├── "
            # Recursively get child lines and extend the list
            child_lines = parse_tree_java(child, indent + 1, child_prefix)
            if child_lines:  # Only add non-empty lines
                lines.extend(child_lines.split("\n"))
    else:
        lines.append(f"{indent_str}{prefix}Unknown node: {tree}")
    
    return "\n".join(line for line in lines if line.strip()) 