from CompiledFiles.commandVisitor import commandVisitor as BaseCommandVisitor

class commandVisitor(BaseCommandVisitor):
    def visitProgram(self, ctx):
        # Handle multiple commands by visiting each one
        result = "0"  # Default result
        for cmd in ctx.command():
            # Visit each command and update the result
            # The last valid command will determine the final result
            cmd_result = self.visit(cmd)
            if cmd_result != "0":  # If it's a valid command
                result = cmd_result
        return result
    
    def visitCommand(self, ctx):
        # Check if this is a non-command (actual code)
        if ctx.non_command():
            return self.visit(ctx.non_command())
        
        # Handle regular commands
        verb_text = ctx.verb().getText()
        args = []
        for noun in ctx.noun():
            args.append(noun.getText())
        
        # Handle translation commands first
        if verb_text == "translate":
            if not ctx.target():
                return "0"  # Invalid: translate without direction
            target = self.visit(ctx.target())
            if target == "python to java":
                return "pytojava"  # Switch to Python to Java mode
            elif target == "java to python":
                return "javatopy"  # Switch to Java to Python mode
            return "0"  # Invalid translation target
            
        # Handle other commands
        elif verb_text in ["save", "store"]:
            return "savecode"  # Save current code
        elif verb_text in ["show", "tell", "see", "retrieve", "get"]:
            if 'output' in args:
                return "showoutput"  # Show output
            elif 'grammar' in args:
                return "showgrammar"  # Show grammar
            return "showsavedcode"  # Show saved code
        
        return "0"  # Invalid command
    
    def visitNon_command(self, ctx):
        # Collect all ID tokens in the non-command
        code_text = ""
        for id_token in ctx.ID():
            code_text += id_token.getText() + " "
        
        # Store the code for processing
        self.code_to_process = code_text.strip()
        
        # Return "0" to indicate this should be handled by code conversion
        return "0"
    
    def visitTarget(self, ctx):
        source = ctx.source().getText()
        target = ctx.target_lang().getText()
        return f"{source} to {target}"