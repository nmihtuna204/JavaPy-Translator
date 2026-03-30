from fastapi import FastAPI
from pydantic import BaseModel
from antlr4 import *
from CompiledFiles.py2javaLexer import py2javaLexer
from CompiledFiles.py2javaParser import py2javaParser
from CompiledFiles.java2pyLexer import java2pyLexer
from CompiledFiles.java2pyParser import java2pyParser
from antlr4.error.ErrorListener import ErrorListener
from fastapi.middleware.cors import CORSMiddleware
from py2javaVisitor import py2javaVisitor
from java2pyVisitor import java2pyVisitor
from tree_printer_py import parse_tree_py
from tree_printer_java import parse_tree_java
from CompiledFiles.commandLexer import commandLexer
from CompiledFiles.commandParser import commandParser
from commandVisitor import commandVisitor
import json
import os
from typing import Optional
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Conversation context storage
conversation_contexts = {}
CONTEXTS_FILE = "conversation_contexts.json"

class CodeInput(BaseModel):
    code: str
    conversation_id: Optional[str] = None

class CustomErrorListener(ErrorListener):
    def __init__(self):
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Syntax error at line {line}:{column}: {msg}")

def load_conversation_contexts():
    """Load conversation contexts from file"""
    global conversation_contexts
    try:
        if os.path.exists(CONTEXTS_FILE):
            with open(CONTEXTS_FILE, 'r') as f:
                conversation_contexts = json.load(f)
    except Exception as e:
        print(f"Error loading contexts: {e}")
        conversation_contexts = {}

def save_conversation_contexts():
    """Save conversation contexts to file"""
    try:
        with open(CONTEXTS_FILE, 'w') as f:
            json.dump(conversation_contexts, f, indent=2)
    except Exception as e:
        print(f"Error saving contexts: {e}")

def get_conversation_context(conversation_id):
    """Get or create conversation context"""
    if conversation_id not in conversation_contexts:
        conversation_contexts[conversation_id] = {
            "last_code": None,
            "last_tree": None,
            "saved_code": None,
            "saved_tree": None,
            "direction": None
        }
    return conversation_contexts[conversation_id]

def set_conversation_context(conversation_id, code, tree):
    """Set the current code and tree for a conversation"""
    context = get_conversation_context(conversation_id)
    context["last_code"] = code
    context["last_tree"] = tree
    save_conversation_contexts()

def set_conversation_direction(conversation_id, direction):
    """Set conversion direction for a conversation"""
    context = get_conversation_context(conversation_id)
    context["direction"] = direction
    save_conversation_contexts()

def save_conversation_code(conversation_id):
    """Save current code for a conversation"""
    context = get_conversation_context(conversation_id)
    context["saved_code"] = context["last_code"]
    context["saved_tree"] = context["last_tree"]
    save_conversation_contexts()

def get_conversation_saved_code(conversation_id):
    """Get saved code for a conversation and set it as current context"""
    context = get_conversation_context(conversation_id)
    saved_code = context["saved_code"]
    saved_tree = context["saved_tree"]
    
    if saved_code is not None:
        # Set the saved code as the current context so subsequent commands work on it
        context["last_code"] = saved_code
        context["last_tree"] = saved_tree
        save_conversation_contexts()
    
    return saved_code

def get_conversation_grammar(conversation_id):
    """Get grammar tree for a conversation"""
    context = get_conversation_context(conversation_id)
    if context["last_tree"] is None:
        return "No tree available for this conversation"
    try:
        if context["direction"] == "pytojava":
            return parse_tree_py(context["last_tree"])
        else:
            return parse_tree_java(context["last_tree"])
    except Exception as e:
        return str(e)

def run_conversation_code(conversation_id):
    """Run code for a specific conversation (supports both Python and Java)"""
    context = get_conversation_context(conversation_id)
    code = context["last_code"]
    direction = context["direction"]
    
    if code is None:
        return "No code available to run for this conversation"
    
    try:
        if direction == "pytojava":
            # Running Python code
            import io
            import sys
            original_stdout = sys.stdout
            captured_output = io.StringIO()
            sys.stdout = captured_output
            
            try:
                local_vars = {}
                exec(code, {}, local_vars)
                output = captured_output.getvalue()
                
                if '__return_value__' in local_vars:
                    output += str(local_vars['__return_value__'])
                    
                return output if output else "Code executed successfully (no output)"
            finally:
                sys.stdout = original_stdout
        
        else:
            # Running Java code (javatopy direction means we're working with Java code)
            return run_java_code(code)
            
    except Exception as e:
        return f"Error executing code: {str(e)}"

def run_java_code(java_code):
    """Compile and run Java code"""
    import subprocess
    import tempfile
    import os
    
    try:
        # Create temporary directory for Java files
        with tempfile.TemporaryDirectory() as temp_dir:
            # Extract class name from Java code
            class_name = extract_java_class_name(java_code)
            if not class_name:
                return "Error: Could not find class name in Java code"
            
            # Write Java code to file
            java_file = os.path.join(temp_dir, f"{class_name}.java")
            with open(java_file, 'w') as f:
                f.write(java_code)
            
            # Compile Java code
            compile_result = subprocess.run(
                ['javac', java_file], 
                capture_output=True, 
                text=True, 
                cwd=temp_dir
            )
            
            if compile_result.returncode != 0:
                return f"Java compilation error:\n{compile_result.stderr}"
            
            # Run Java code
            run_result = subprocess.run(
                ['java', class_name], 
                capture_output=True, 
                text=True, 
                cwd=temp_dir,
                timeout=10  # 10 second timeout
            )
            
            if run_result.returncode != 0:
                return f"Java runtime error:\n{run_result.stderr}"
            
            return run_result.stdout if run_result.stdout else "Java code executed successfully (no output)"
            
    except subprocess.TimeoutExpired:
        return "Error: Java code execution timed out (10 seconds)"
    except FileNotFoundError:
        return "Error: Java compiler (javac) not found. Please ensure Java is installed and in PATH."
    except Exception as e:
        return f"Error running Java code: {str(e)}"

def extract_java_class_name(java_code):
    """Extract the main class name from Java code"""
    import re
    
    # Look for public class declaration
    public_class_match = re.search(r'public\s+class\s+(\w+)', java_code)
    if public_class_match:
        return public_class_match.group(1)
    
    # Look for any class declaration
    class_match = re.search(r'class\s+(\w+)', java_code)
    if class_match:
        return class_match.group(1)
    
    return None

def detect_code_language(code):
    """Detect the language of the input code"""
    # Remove comments and whitespace for better detection
    code_clean = code.strip().lower()
    
    # Java indicators
    java_indicators = [
        'public class',
        'private class', 
        'protected class',
        'public static void main',
        'system.out.println',
        'string[]',
        'public void',
        'private void',
        'import java.',
        '.java'
    ]
    
    # Python indicators
    python_indicators = [
        'def ',
        'print(',
        'if __name__',
        'import ',
        'from ',
        ':',  # Python uses colons for blocks
        'elif',
        'lambda',
        '.py'
    ]
    
    java_score = sum(1 for indicator in java_indicators if indicator in code_clean)
    python_score = sum(1 for indicator in python_indicators if indicator in code_clean)
    
    # Additional heuristics
    if '{' in code and '}' in code and ';' in code:
        java_score += 2
    if code_clean.count(':') > code_clean.count(';'):
        python_score += 1
        
    if java_score > python_score:
        return 'java'
    elif python_score > java_score:
        return 'python'
    else:
        return 'unknown'

def validate_code_direction(code, direction):
    """Validate if code language matches the conversion direction"""
    detected_language = detect_code_language(code)
    
    if direction == "pytojava" and detected_language == "java":
        return {
            "valid": False,
            "message": "You are in Python to Java mode, but entered Java code. If you want to convert Java to Python, please use the command 'translate java to python'."
        }
    elif direction == "javatopy" and detected_language == "python":
        return {
            "valid": False, 
            "message": "You are in Java to Python mode, but entered Python code. If you want to convert Python to Java, please use the command 'translate python to java'."
        }
    
    return {"valid": True}

# Handle code conversion for a specific conversation
def handle_conversation_code(conversation_id, code):
    """Handle code conversion for a specific conversation"""
    context = get_conversation_context(conversation_id)
    direction = context["direction"]
    
    # Validate code language matches direction
    validation = validate_code_direction(code, direction)
    if not validation["valid"]:
        return {
            "error": validation["message"],
            "type": "language_mismatch"
        }
    
    try:
        if direction == "pytojava":
            # Python to Java conversion
            input_stream = InputStream(code)
            lexer = py2javaLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            
            parser = py2javaParser(token_stream)
            parser.removeErrorListeners()
            error_listener = CustomErrorListener()
            parser.addErrorListener(error_listener)
            tree = parser.program()
            
            if error_listener.errors:
                return {"error": error_listener.errors}
            
            # Store the tree and code for this conversation
            set_conversation_context(conversation_id, code, tree)
            
            # Convert to Java
            visitor = py2javaVisitor()
            java_code = visitor.visit(tree)
            return java_code
        elif direction == "javatopy":
            # Java to Python conversion
            input_stream = InputStream(code)
            lexer = java2pyLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            
            parser = java2pyParser(token_stream)
            parser.removeErrorListeners()
            error_listener = CustomErrorListener()
            parser.addErrorListener(error_listener)
            tree = parser.program()
            
            if error_listener.errors:
                return {"error": error_listener.errors}
            
            # Store the tree and code for this conversation
            set_conversation_context(conversation_id, code, tree)
            
            # Convert to Python
            visitor = java2pyVisitor()
            python_code = visitor.visit(tree)
            return python_code
        
    except Exception as e:
        return {"error": str(e)}

# Load contexts on startup
load_conversation_contexts()

def response_message(result):
    if result == "0":
        messages = [
                "I've translated your code! Here's what I came up with:",
                "Great code! I've converted it for you. Take a look:",
                "All done with the conversion! Check out the result:"
            ]
        return random.choice(messages)
    elif result == "savecode":
        messages = [
            "Code saved successfully for this conversation",
            "I've saved your code. You can retrieve it later using the 'show saved code' command",
            "Your code is now saved. Use 'show saved code' to view it anytime"
        ]
        return random.choice(messages)
    elif result == "showsavedcode":
        messages = [
            "Here is your saved code:",
            "I've retrieved your saved code. Here it is:",
            "Here is the code you saved earlier:"
        ]
        return random.choice(messages)
    elif result == "showgrammar":
        messages = [
            "Here is the parse tree for your code:",
            "Let me show you the parse tree representation:",
            "Take a look at the parse tree I generated:"
        ]
        return random.choice(messages)
    elif result == "showoutput":
        messages = [
            "Here's what happened when I ran your code:",
            "Check out what your code produced:",
            "The execution results are in - take a look:"
        ]
        return random.choice(messages)
    elif result == "javatopy":
        messages = [
            "Switched to Java to Python conversion mode for this conversation",
            "I've switched to Java to Python mode for this conversation",
            "Now ready to convert Java code to Python for this conversation"
        ]
        return random.choice(messages)
    elif result == "pytojava":
        messages = [
            "Switched to Python to Java conversion mode for this conversation",
            "I've switched to Python to Java mode for this conversation",
            "Now ready to convert Python code to Java for this conversation"
        ]   
        return random.choice(messages)
    else:
        return "I'm sorry, I don't understand that command. Please try again."

@app.post("/convert")
async def convert_code(input_data: CodeInput):
    try:
        conversation_id = input_data.conversation_id or "default"
        
        # First try to parse as a command
        cleaned_code = input_data.code.rstrip() + "\n"
        input_stream = InputStream(cleaned_code)
        lexer = commandLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = commandParser(stream)
        error_listener = CustomErrorListener()
        parser.addErrorListener(error_listener)
        tree = parser.program()

        # Visit and handle command
        visitor = commandVisitor()
        result = visitor.visit(tree)

        # If it's not a valid command and we have a direction set, try code conversion
        if result == "0":
            converted_code = handle_conversation_code(conversation_id, input_data.code)
            
            return {
                "result": converted_code,
                "type": "converted_code", 
                "message": response_message(result),
                "conversation_id": conversation_id
            }
                
        elif result == "savecode":  # Save current code for this conversation
            save_conversation_code(conversation_id)
            return {
                "result": response_message(result), 
                "type": "message",
                "conversation_id": conversation_id
            }
            
        elif result == "showsavedcode":  # Show saved code for this conversation
            saved_code = get_conversation_saved_code(conversation_id)
            if saved_code is not None:
                return {
                    "result": saved_code, 
                    "type": "code",
                    "message": response_message(result),
                    "conversation_id": conversation_id
                }
            else:
                return {
                    "result": "No saved code for this conversation", 
                    "type": "message",
                    "conversation_id": conversation_id
                }
            
        elif result == "showgrammar":  # Show parse tree for this conversation
            code = get_conversation_grammar(conversation_id)
            return {
                "result": code, 
                "type": "grammar",
                "message": response_message(result),
                "conversation_id": conversation_id
            }
            
        elif result == "showoutput":  # Show output for this conversation
            output = run_conversation_code(conversation_id)
            return {
                "result": output, 
                "type": "output", 
                "message": "Okay, here is your output:",
                "conversation_id": conversation_id
            }
            
        elif result == "javatopy":  # Switch to Java to Python mode for this conversation
            set_conversation_direction(conversation_id, "javatopy")
            return {
                "result": "I've switched to Java to Python mode for this conversation. You can now enter Java code and I'll convert it to Python.", 
                "type": "message",
                "conversation_id": conversation_id,
                "direction": "javatopy"
            }
            
        elif result == "pytojava":  # Switch to Python to Java mode for this conversation
            set_conversation_direction(conversation_id, "pytojava")
            return {
                "result": "I've switched to Python to Java mode for this conversation. You can now enter Python code and I'll convert it to Java.", 
                "type": "message",
                "conversation_id": conversation_id,
                "direction": "pytojava"
            }
            
        # Try code conversion as fallback
        converted_code = handle_conversation_code(conversation_id, input_data.code)
        return {
            "result": converted_code,
            "type": "converted_code", 
            "conversation_id": conversation_id
        }
        
    except Exception as e:
        return {"error": str(e)}

@app.get("/conversation/{conversation_id}/context")
async def get_conversation_info(conversation_id: str):
    """Get conversation context information"""
    context = get_conversation_context(conversation_id)
    return {
        "conversation_id": conversation_id,
        "has_code": context["last_code"] is not None,
        "has_saved_code": context["saved_code"] is not None,
        "direction": context["direction"],
        "last_code_preview": context["last_code"][:100] + "..." if context["last_code"] and len(context["last_code"]) > 100 else context["last_code"]
    }