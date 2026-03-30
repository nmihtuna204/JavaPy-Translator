from CompiledFiles.py2javaVisitor import py2javaVisitor
from CompiledFiles.py2javaLexer import py2javaLexer
from CompiledFiles.py2javaParser import py2javaParser

class py2javaVisitor(py2javaVisitor):
    def visitProgram(self, ctx):
        lines = []
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, py2javaParser.StmtContext):
                lines.append(self.visit(child))
            # Skip NL tokens
        return "\n".join(line for line in lines if line.strip())

    def visitStmt(self, ctx):
        if ctx.asg():
            return self.visit(ctx.asg())
        elif ctx.ifStmt():
            return self.visit(ctx.ifStmt())
        elif ctx.funcStmt():
            return self.visit(ctx.funcStmt())
        elif ctx.whileStmt():
            return self.visit(ctx.whileStmt())
        elif ctx.forStmt():
            return self.visit(ctx.forStmt())
        elif ctx.breakStmt():
            return self.visit(ctx.breakStmt())
        elif ctx.postfixStmt():
            return self.visit(ctx.postfixStmt())
        elif ctx.returnStmt():
            return self.visit(ctx.returnStmt())
        elif ctx.mainStmt():
            return self.visit(ctx.mainStmt())
        elif ctx.printStmt():
            return self.visit(ctx.printStmt())
        elif ctx.callStmt():
            return self.visit(ctx.callStmt())
        elif ctx.questStmt():
            return self.visit(ctx.questStmt())
        else:
            return ""

    def visitForStmt(self, ctx):
        var = ctx.ID().getText()
        range_exp = self.visit(ctx.rangeExp())
        block_code = self.visit(ctx.block())
        return f"{range_exp[0]} {var} {range_exp[1]} {{\n{block_code}\n}}"

    def visitRangeExp(self, ctx):
        args = [self.visit(exp) for exp in ctx.exp()]
        if len(args) == 1:  # range(stop)
            return (f"for (int", f"= 0; {args[0]} < {args[0]}; {args[0]}++)")
        elif len(args) == 2:  # range(start, stop)
            return (f"for (int", f"= {args[0]}; {args[0]} < {args[1]}; {args[0]}++)")
        else:  # range(start, stop, step)
            return (f"for (int", f"= {args[0]}; {args[0]} < {args[1]}; {args[0]} += {args[2]})")

    def visitCallStmt(self, ctx):
        func_name = ctx.ID().getText()
        arg = self.visit(ctx.exp()) if ctx.exp() else ""
        return f"{func_name}({arg});"

    def visitAsg(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.exp())
        # Check if the expression resolves to a STRING, FLOAT, or other type
        type_str = self.inferType(ctx.exp())
        return f"{type_str} {var_name} = {value};"

    def inferType(self, ctx):
        # Try to determine the type of expression
        if not ctx:
            return "int"  # Default

        if isinstance(ctx, py2javaParser.ExpContext):
            return self.inferType(ctx.logicExp())
        elif isinstance(ctx, py2javaParser.LogicExpContext):
            if ctx.op and (ctx.op.text == "and" or ctx.op.text == "or"):
                return "boolean"
            return self.inferType(ctx.compExp(0))
        elif isinstance(ctx, py2javaParser.CompExpContext):
            if ctx.op:
                return "boolean"
            return self.inferType(ctx.addExp(0))
        elif isinstance(ctx, py2javaParser.AddExpContext):
            return self.inferType(ctx.mulExp(0))
        elif isinstance(ctx, py2javaParser.MulExpContext):
            return self.inferType(ctx.unaryExp(0))
        elif isinstance(ctx, py2javaParser.UnaryExpContext):
            if ctx.op and ctx.op.text == "not":
                return "boolean"
            return self.inferType(ctx.atom()) if ctx.atom() else self.inferType(ctx.unaryExp())
        elif isinstance(ctx, py2javaParser.AtomContext):
            if ctx.STRING():
                return "String"
            elif ctx.FLOAT():
                return "double"
            elif ctx.TRUE() or ctx.FALSE():
                return "boolean"
            elif ctx.NONE():
                return "Object"
            elif ctx.NUMBER():
                return "int"
            elif ctx.ID():
                if ctx.postfix():
                    return "int" 
                if ctx.getChildCount() > 1 and ctx.getChild(1).getText() == '(':
                    # Function call, assume int return type
                    return "int"
                return "int"  # Default for identifiers
            elif ctx.exp():
                return self.inferType(ctx.exp())
            return "int"  # Default
        return "int"  # Default fallback

    def visitReturnStmt(self, ctx):
        value = self.visit(ctx.exp())
        return f"return {value};"

    def visitPostfixStmt(self, ctx):
        var = ctx.ID().getText()
        op = self.visit(ctx.postfix())
        if ctx.exp():
            arg = self.visit(ctx.exp())
            return f"{var} {op} {arg};"
        return f"{var}{op};"

    def visitPostfix(self, ctx):
        return ctx.op.text

    def visitLogicExp(self, ctx):
        if not ctx.op:
            return self.visit(ctx.compExp(0))
        
        left = self.visit(ctx.compExp(0))
        right = self.visit(ctx.compExp(1))
        if ctx.op.text == "and":
            return f"{left} && {right}"
        elif ctx.op.text == "or":
            return f"{left} || {right}"
        return f"{left} {ctx.op.text} {right}"

    def visitCompExp(self, ctx):
        if not ctx.op:
            return self.visit(ctx.addExp(0))
        
        left = self.visit(ctx.addExp(0))
        right = self.visit(ctx.addExp(1))
        return f"{left} {ctx.op.text} {right}"

    def visitAddExp(self, ctx):
        if not ctx.op:
            return self.visit(ctx.mulExp(0))
        
        left = self.visit(ctx.mulExp(0))
        right = self.visit(ctx.mulExp(1))
        return f"({left} {ctx.op.text} {right})"

    def visitMulExp(self, ctx):
        if not ctx.op:
            return self.visit(ctx.unaryExp(0))
        
        left = self.visit(ctx.unaryExp(0))
        right = self.visit(ctx.unaryExp(1))
        return f"({left} {ctx.op.text} {right})"

    def visitUnaryExp(self, ctx):
        if ctx.op:
            op = ctx.op.text
            java_op = "!" if op == "not" else op
            operand = self.visit(ctx.unaryExp())
            return f"{java_op}{operand}"
        return self.visit(ctx.atom())

    def visitAtom(self, ctx):
        if ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.FLOAT():
            return ctx.FLOAT().getText()
        elif ctx.TRUE():
            return "true"
        elif ctx.FALSE():
            return "false"
        elif ctx.NONE():
            return "null"
        elif ctx.STRING():
            return ctx.STRING().getText()
        elif ctx.ID():
            if ctx.getChildCount() > 1 and ctx.getChild(1).getText() == '(':
                # Function call: ID(exp, exp, ...)
                func_name = ctx.ID().getText()
                args = []
                exp_list = ctx.exp() if ctx.exp() else []
                if isinstance(exp_list, list):
                    for exp in exp_list:
                        args.append(self.visit(exp))
                else:
                    args.append(self.visit(exp_list))
                return f"{func_name}({', '.join(args)})"
            elif ctx.postfix():
                # With postfix
                return f"{ctx.ID().getText()}{self.visit(ctx.postfix())}"
            return ctx.ID().getText()
        elif ctx.getChild(0).getText() == '(' and ctx.getChild(2).getText() == ')':
            # Expression in parentheses: (exp)
            exp_ctx = ctx.exp()
            if isinstance(exp_ctx, list):
                if len(exp_ctx) == 1:
                    return self.visit(exp_ctx[0])
                else:
                    raise Exception("Expected exactly one expression in parentheses")
            return self.visit(exp_ctx)
        raise Exception(f"Unsupported atom: {ctx.getText()}")

    def visitExp(self, ctx):
        return self.visit(ctx.logicExp())

    def visitIfStmt(self, ctx):
        condition = self.visit(ctx.exp())
        block_code = self.visit(ctx.block())
        block_lines = block_code.split("\n")
        indented_block = "\n".join("    " + line for line in block_lines if line.strip())
        elif_parts = ""
        if ctx.elifStmt():
            for elif_ctx in ctx.elifStmt():
                elif_part = self.visit(elif_ctx)
                elif_parts += f"\n{elif_part}"
        else_part = ""
        if ctx.elseStmt():
            else_part = self.visit(ctx.elseStmt())
            else_part = f"\n{else_part}"
        return f"if ({condition}) {{\n{indented_block}\n}}{elif_parts}{else_part}"

    def visitElifStmt(self, ctx):
        condition = self.visit(ctx.exp())
        block_code = self.visit(ctx.block())
        block_lines = block_code.split("\n")
        indented_block = "\n".join("    " + line for line in block_lines if line.strip())
        return f"else if ({condition}) {{\n{indented_block}\n}}"

    def visitElseStmt(self, ctx):
        block_code = self.visit(ctx.block())
        block_lines = block_code.split("\n")
        indented_block = "\n".join("    " + line for line in block_lines if line.strip())
        return f"else {{\n{indented_block}\n}}"

    def visitFuncStmt(self, ctx):
        func_name = ctx.ID().getText()
        params = self.visit(ctx.param()) if ctx.param() else ""
        block_code = self.visit(ctx.block())
        block_lines = block_code.split("\n")
        indented_block = "\n".join("    " + line for line in block_lines if line.strip())
        return f"public static int {func_name}({params}) {{\n{indented_block}\n}}"

    def visitWhileStmt(self, ctx):
        condition = self.visit(ctx.exp())
        block_code = self.visit(ctx.block())
        return f"while ({condition}) {{\n{block_code}\n}}"

    def visitPrintStmt(self, ctx):
        if not ctx.printArgs():
            return "System.out.println();"
        args = []
        for exp_ctx in ctx.printArgs().exp():
            args.append(self.visit(exp_ctx))
        if len(args) == 1:
            return f"System.out.println({args[0]});"
        # Handle string concatenation
        return f"System.out.println({' + '.join(args)});"

    def visitMainStmt(self, ctx):
        block_code = self.visit(ctx.block())
        block_lines = block_code.split("\n")
        indented_block = "\n".join("    " + line for line in block_lines if line.strip())
        return f"public static void main(String[] args) {{\n{indented_block}\n}}"

    def visitBreakStmt(self, ctx):
        return "break;"

    def visitBlock(self, ctx):
        indent = "    "
        return "\n".join(indent + self.visit(stmt) for stmt in ctx.stmt())

    def visitParam(self, ctx):
        return ", ".join(f"int {id.getText()}" for id in ctx.ID())

    def visitQuestStmt(self, ctx):
        verb_text = ctx.verb().getText()
        args = []
        for noun in ctx.noun():
            args.append(noun.getText())
        
        
        # Handle show/tell commands
        if verb_text in ["retrieve", "get"]:
            return "1"  # Return code for showing parse tree
        # Handle save command
        elif verb_text in ["save", "store"]:
            return "2"  # Return code for saving code
        # Handle get saved code command
        elif verb_text in ["show", "tell"]:
            if 'output' in args:
                return "4"  # show the output of the code
            return "3"  # Return code for retrieving saved code
        # Unknown command
        else:
            return "0"  # Return code for invalid command