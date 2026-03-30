from CompiledFiles.java2pyVisitor import java2pyVisitor
from CompiledFiles.java2pyLexer import java2pyLexer
from CompiledFiles.java2pyParser import java2pyParser

class java2pyVisitor(java2pyVisitor):
    def __init__(self):
        self.indent_level = 0

    def indent(self):
        return "    " * self.indent_level

    def visitProgram(self, ctx):
        # A program consists of a class definition
        return self.visit(ctx.classDef())

    def visitClassDef(self, ctx):
        # Extract the class name (though Python doesn't need it for this translation)
        class_name = ctx.ID().getText()
        # Process the class body (which contains methods)
        return self.visit(ctx.classBody())

    def visitClassBody(self, ctx):
        # Process all method definitions in the class body
        lines = []
        for method in ctx.methodDef():
            method_code = self.visit(method)
            if method_code:
                lines.append(method_code)
        return "\n".join(lines)

    def visitMethodDef(self, ctx):
        # Handle method definitions (including main)
        method_name = ctx.ID().getText()
        params = self.visit(ctx.param()) if ctx.param() else ""
        # Handle the block
        self.indent_level += 1
        block_code = self.visit(ctx.block())
        self.indent_level -= 1
        # If this is the main method, translate to Python's if __name__ == "__main__":
        if method_name == "main" and ctx.javaType().getText() == "void":
            return f"if __name__ == '__main__':\n{block_code}"
        # Otherwise, define a Python function
        return f"def {method_name}({params}):\n{block_code}"

    def visitStmt(self, ctx):
        if ctx.whileStmt():
            return self.visit(ctx.whileStmt())
        elif ctx.forStmt():
            return self.visit(ctx.forStmt())
        elif ctx.ifStmt():
            return self.visit(ctx.ifStmt())
        elif ctx.funcStmt():
            return self.visit(ctx.funcStmt())
        elif ctx.asg():
            return self.visit(ctx.asg())
        elif ctx.breakStmt():
            return self.visit(ctx.breakStmt())
        elif ctx.postfixStmt():
            return self.visit(ctx.postfixStmt())
        elif ctx.returnStmt():
            return self.visit(ctx.returnStmt())
        elif ctx.printStmt():
            return self.visit(ctx.printStmt())
        elif ctx.callStmt():
            return self.visit(ctx.callStmt())
        return ""

    def visitWhileStmt(self, ctx):
        condition = self.visit(ctx.exp())
        self.indent_level += 1
        block_code = self.visit(ctx.block())
        self.indent_level -= 1
        return f"{self.indent()}while {condition}:\n{block_code}"

    def visitForStmt(self, ctx):
        # Extract components of the for loop
        # Initialization: javaType ID '=' exp
        var_name = ctx.ID().getText()
        init_value = self.visit(ctx.getChild(4))  # exp after '='
        init = f"{var_name} = {init_value}"
        # Condition: exp (second expression after ';')
        condition = self.visit(ctx.getChild(6))
        # Update: postfixStmt (third part before ')')
        update = self.visit(ctx.postfixStmt())
        # Block
        self.indent_level += 1
        block_code = self.visit(ctx.block())
        self.indent_level -= 1
        # Convert to while loop
        return f"{self.indent()}# Converted from Java for loop\n{self.indent()}{init}\n{self.indent()}while {condition}:\n{block_code}\n{self.indent()}    {update}"

    def visitIfStmt(self, ctx):
        condition = self.visit(ctx.exp())
        self.indent_level += 1
        block_code = self.visit(ctx.block())
        self.indent_level -= 1
        elif_parts = ""
        for elif_ctx in ctx.elifStmt():
            elif_part = self.visit(elif_ctx)
            elif_parts += f"\n{elif_part}"
        else_part = ""
        if ctx.elseStmt():
            else_part = f"\n{self.visit(ctx.elseStmt())}"
        return f"{self.indent()}if {condition}:\n{block_code}{elif_parts}{else_part}"

    def visitElifStmt(self, ctx):
        condition = self.visit(ctx.exp())
        self.indent_level += 1
        block_code = self.visit(ctx.block())
        self.indent_level -= 1
        return f"{self.indent()}elif {condition}:\n{block_code}"

    def visitElseStmt(self, ctx):
        self.indent_level += 1
        block_code = self.visit(ctx.block())
        self.indent_level -= 1
        return f"{self.indent()}else:\n{block_code}"

    def visitFuncStmt(self, ctx):
        func_name = ctx.ID().getText()
        params = self.visit(ctx.param()) if ctx.param() else ""
        self.indent_level += 1
        block_code = self.visit(ctx.block())
        self.indent_level -= 1
        return f"{self.indent()}def {func_name}({params}):\n{block_code}"

    def visitAsg(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.exp())
        return f"{self.indent()}{var_name} = {value}"

    def visitBreakStmt(self, ctx):
        return f"{self.indent()}break"

    def visitPostfixStmt(self, ctx):
        var = ctx.ID().getText()
        op = ctx.op.text
        if op == "++":
            return f"{self.indent()}{var} += 1"
        elif op == "--":
            return f"{self.indent()}{var} -= 1"
        elif ctx.exp():
            arg = self.visit(ctx.exp())
            return f"{self.indent()}{var} {op} {arg}"
        return f"{self.indent()}{var}{op}"

    def visitReturnStmt(self, ctx):
        value = self.visit(ctx.exp())
        return f"{self.indent()}return {value}"

    def visitPrintStmt(self, ctx):
        if not ctx.printArgs():
            return f"{self.indent()}print()"
        args = [self.visit(exp) for exp in ctx.printArgs().exp()]
        return f"{self.indent()}print({', '.join(args)})"

    def visitCallStmt(self, ctx):
        func_name = ctx.ID().getText()
        args = [self.visit(exp) for exp in ctx.exp()] if ctx.exp() else []
        return f"{self.indent()}{func_name}({', '.join(args)})"

    def visitBlock(self, ctx):
        lines = []
        for stmt in ctx.stmt():
            stmt_code = self.visit(stmt)
            if stmt_code:
                lines.append(stmt_code)
        return "\n".join(lines)

    def visitParam(self, ctx):
        return ", ".join(id.getText() for id in ctx.ID())

    def visitExp(self, ctx):
        return self.visit(ctx.logicExp())

    def visitLogicExp(self, ctx):
        if not ctx.op:  # Base case: just a compExp
            return self.visit(ctx.compExp())
        # Recursive case: logicExp op compExp
        left = self.visit(ctx.logicExp())
        right = self.visit(ctx.compExp())
        op = ctx.op.text
        if op == "&&":
            op = "and"
        elif op == "||":
            op = "or"
        return f"{left} {op} {right}"

    def visitCompExp(self, ctx):
        if not ctx.op:  # Base case: just an addExp
            return self.visit(ctx.addExp())
        # Recursive case: compExp op addExp
        left = self.visit(ctx.compExp())
        right = self.visit(ctx.addExp())
        op = ctx.op.text
        return f"{left} {op} {right}"

    def visitAddExp(self, ctx):
        if not ctx.op:  # Base case: just a mulExp
            return self.visit(ctx.mulExp())
        # Recursive case: addExp op mulExp
        left = self.visit(ctx.addExp())
        right = self.visit(ctx.mulExp())
        op = ctx.op.text
        return f"({left} {op} {right})"

    def visitMulExp(self, ctx):
        if not ctx.op:  # Base case: just a unaryExp
            return self.visit(ctx.unaryExp())
        # Recursive case: mulExp op unaryExp
        left = self.visit(ctx.mulExp())
        right = self.visit(ctx.unaryExp())
        op = ctx.op.text
        return f"({left} {op} {right})"

    def visitUnaryExp(self, ctx):
        if ctx.op:
            op = ctx.op.text
            python_op = "not " if op == "!" else op
            operand = self.visit(ctx.unaryExp())
            return f"{python_op}{operand}"
        return self.visit(ctx.atom())

    def visitAtom(self, ctx):
        if ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.FLOAT():
            return ctx.FLOAT().getText()
        elif ctx.TRUE():
            return "True"
        elif ctx.FALSE():
            return "False"
        elif ctx.NULL():
            return "None"
        elif ctx.STRING():
            return ctx.STRING().getText()
        elif ctx.ID():
            id_text = ctx.ID().getText()
            if ctx.postfix():
                op = ctx.postfix().op.text
                if op == "++":
                    return f"({id_text} := {id_text} + 1)"
                elif op == "--":
                    return f"({id_text} := {id_text} - 1)"
                return f"{id_text}{op}"
            elif ctx.getChildCount() > 1 and ctx.getChild(1).getText() == '(':
                # Function call
                args = [self.visit(exp) for exp in ctx.exp()] if ctx.exp() else []
                return f"{id_text}({', '.join(args)})"
            return id_text
        elif ctx.exp():
            return f"({self.visit(ctx.exp())})"
        raise Exception(f"Unsupported atom: {ctx.getText()}")