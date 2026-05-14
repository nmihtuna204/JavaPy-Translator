from antlr4 import ParserRuleContext, TerminalNode
from CompiledFiles.py2javaLexer import py2javaLexer
from CompiledFiles.py2javaParser import py2javaParser

# Create a direct mapping from token types to names based on projLexer.tokens
TOKEN_TYPE_MAP = {
    1: "LPAREN",
    2: "COMMA",
    3: "RPAREN",
    4: "AND",
    5: "OR",
    6: "GT",
    7: "LT",
    8: "EQ",
    9: "NEQ",
    10: "LTE",
    11: "GTE",
    12: "PLUS",
    13: "MINUS",
    14: "MUL",
    15: "DIV",
    16: "NOT",
    17: "DEC",
    18: "INC",
    19: "PLUSEQ",
    20: "MINEQ",
    21: "MAIN",
    22: "DEF",
    23: "IF",
    24: "ELIF",
    25: "ELSE",
    26: "COLON",
    27: "BREAK",
    28: "WHILE",
    29: "FOR",
    30: "IN",
    31: "RANGE",
    32: "RETURN",
    33: "PRINT",
    34: "TRUE",
    35: "FALSE",
    36: "NONE",
    37: "STRING",
    38: "ID",
    39: "EQUAL",
    40: "NUMBER",
    41: "FLOAT",
    42: "NL",
    43: "WS"
}

def parse_tree_py(tree, indent=0, prefix=""):
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
        if token_type in [46, 47]:  # NL or WS
            return ""
            
        # Get token name from the map or use a default
        token_name = TOKEN_TYPE_MAP.get(token_type, f"UNKNOWN({token_type})")
            
        lines.append(f"{indent_str}{prefix}Token: {token_text} (type: {token_name})")
    elif isinstance(tree, ParserRuleContext):
        # Rule node (e.g., program, stmt, asg)
        rule_name = py2javaParser.ruleNames[tree.getRuleIndex()]
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
            child_lines = parse_tree_py(child, indent + 1, child_prefix)
            if child_lines:  # Only add non-empty lines
                lines.extend(child_lines.split("\n"))
    else:
        lines.append(f"{indent_str}{prefix}Unknown node: {tree}")
    
    return "\n".join(line for line in lines if line.strip())