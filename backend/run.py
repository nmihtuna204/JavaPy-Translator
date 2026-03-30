import sys, os
import subprocess
import unittest
from antlr4 import *
from tree_printer_py import parse_tree_py
from tree_printer_java import parse_tree_java

# Define your variables
DIR = os.path.dirname(__file__)
ANTLR_JAR = 'C:/antlr/antlr4-4.9.2-complete.jar'  # Consider making this configurable
CPL_Dest = 'CompiledFiles'
PY2JAVA_SRC = 'py2java.g4'
JAVA2PY_SRC = 'java2py.g4'
COMMAND_SRC = 'command.g4'
TESTS = os.path.join(DIR, './tests')

def printUsage():
    print('python run.py gen')
    print('python run.py test [py|java|command] [test_file]')
    print('python run.py command <command>')
    print('  py      - Test Python to Java conversion (default: 001.txt)')
    print('  java    - Test Java to Python conversion (default: 002.txt)')
    print('  command - Test command grammar (default: 003.txt)')
    print('  test_file - Optional test file name (e.g., 003.txt)')
    print('  command - Command (e.g., "show output", "save code", etc.)')

def printBreak():
    print('-----------------------------------------------')

def generateAntlr2Python():
    print('Generating py2java grammar...')
    try:
        result = subprocess.run(['java', '-jar', ANTLR_JAR, '-o', CPL_Dest, '-no-listener', '-Dlanguage=Python3', '-visitor', PY2JAVA_SRC], check=True, capture_output=True, text=True)
        print(result.stdout)
        print('py2java grammar generated successfully')
    except FileNotFoundError:
        print(f"Error: ANTLR jar not found at {ANTLR_JAR}")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error generating py2java grammar: {e.stderr}")
        sys.exit(1)

    print('Generating java2py grammar...')
    try:
        result = subprocess.run(['java', '-jar', ANTLR_JAR, '-o', CPL_Dest, '-no-listener', '-Dlanguage=Python3', '-visitor', JAVA2PY_SRC], check=True, capture_output=True, text=True)
        print(result.stdout)
        print('java2py grammar generated successfully')
    except subprocess.CalledProcessError as e:
        print(f"Error generating java2py grammar: {e.stderr}")
        sys.exit(1)

    print('Generating command grammar...')
    try:
        result = subprocess.run(['java', '-jar', ANTLR_JAR, '-o', CPL_Dest, '-no-listener', '-Dlanguage=Python3', '-visitor', COMMAND_SRC], check=True, capture_output=True, text=True)
        print(result.stdout)
        print('command grammar generated successfully')
    except subprocess.CalledProcessError as e:
        print(f"Error generating command grammar: {e.stderr}")
        sys.exit(1)

    print('All grammars generated successfully')

def runPythonTest(filename='001.txt'):
    # Check if CompiledFiles exists
    if not os.path.exists(CPL_Dest):
        print(f"Error: {CPL_Dest} directory not found. Run 'python run.py gen' first.")
        sys.exit(1)

    try:
        from py2javaVisitor import py2javaVisitor
        from CompiledFiles.py2javaLexer import py2javaLexer
        from CompiledFiles.py2javaParser import py2javaParser
    except ImportError as e:
        print(f"Error: Failed to import py2java modules. Ensure grammars are generated: {e}")
        sys.exit(1)

    from antlr4.error.ErrorListener import ErrorListener

    print('Running Python to Java test...')

    class CustomErrorListener(ErrorListener):
        def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
            print(f"Input rejected: {msg} at line {line}, column {column}")
            sys.exit(1)

    inputFile = os.path.join(DIR, './tests', filename)
    if not os.path.exists(inputFile):
        print(f"Error: Test file {inputFile} not found.")
        sys.exit(1)

    # Test
    input_stream = FileStream(inputFile)
    lexer = py2javaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = py2javaParser(stream)
    parser.addErrorListener(CustomErrorListener())  # Attach error listener
    tree = parser.program()

    # Print the parse tree (for debugging)
    parse_tree_output = parse_tree_py(tree)
    print(parse_tree_output)

    # Visit and print converted code
    visitor = py2javaVisitor()
    java_code = visitor.visit(tree)
    print("// Translated Java code:")
    print(java_code)

    printBreak()
    print('Python to Java test completed')

def runJavaTest(filename='002.txt'):
    # Check if CompiledFiles exists
    if not os.path.exists(CPL_Dest):
        print(f"Error: {CPL_Dest} directory not found. Run 'python run.py gen' first.")
        sys.exit(1)

    try:
        from java2pyVisitor import java2pyVisitor
        from CompiledFiles.java2pyLexer import java2pyLexer
        from CompiledFiles.java2pyParser import java2pyParser
    except ImportError as e:
        print(f"Error: Failed to import java2py modules. Ensure grammars are generated: {e}")
        sys.exit(1)

    from antlr4.error.ErrorListener import ErrorListener

    print('Running Java to Python test...')

    class CustomErrorListener(ErrorListener):
        def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
            print(f"Input rejected: {msg} at line {line}, column {column}")
            sys.exit(1)

    inputFile = os.path.join(DIR, './tests', filename)
    if not os.path.exists(inputFile):
        print(f"Error: Test file {inputFile} not found.")
        sys.exit(1)

    # Test
    input_stream = FileStream(inputFile)
    lexer = java2pyLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = java2pyParser(stream)
    parser.addErrorListener(CustomErrorListener())  # Attach error listener
    tree = parser.program()

    # Print the parse tree (for debugging)
    parse_tree_output = parse_tree_java(tree)
    print(parse_tree_output)

    # Visit and print converted code
    visitor = java2pyVisitor()
    python_code = visitor.visit(tree)
    print("# Translated Python code:")
    print(python_code)

    printBreak()
    print('Java to Python test completed')

def runCommandTest(filename='003.txt'):
    # Check if CompiledFiles exists
    if not os.path.exists(CPL_Dest):
        print(f"Error: {CPL_Dest} directory not found. Run 'python run.py gen' first.")
        sys.exit(1)

    try:
        from commandVisitor import commandVisitor
        from CompiledFiles.commandLexer import commandLexer
        from CompiledFiles.commandParser import commandParser
    except ImportError as e:
        print(f"Error: Failed to import command modules. Ensure grammars are generated: {e}")
        sys.exit(1)

    from antlr4.error.ErrorListener import ErrorListener

    print('Running Command grammar test...')

    class CustomErrorListener(ErrorListener):
        def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
            print(f"Input rejected: {msg} at line {line}, column {column}")
            sys.exit(1)

    inputFile = os.path.join(DIR, './tests', filename)
    if not os.path.exists(inputFile):
        print(f"Error: Test file {inputFile} not found.")
        sys.exit(1)

    # Test
    input_stream = FileStream(inputFile)
    lexer = commandLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = commandParser(stream)
    parser.addErrorListener(CustomErrorListener())
    tree = parser.program()

    # Visit and print command result
    visitor = commandVisitor()
    result = visitor.visit(tree)
    print("Command Result Code:", result)

    printBreak()
    print('Command grammar test completed')

def main(argv):
    print('Complete jar file ANTLR  :  ' + str(ANTLR_JAR))
    print('Length of arguments      :  ' + str(len(argv)))
    printBreak()

    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'gen':
        # Check if ANTLR jar exists
        if not os.path.exists(ANTLR_JAR):
            print(f"Error: ANTLR jar not found at {ANTLR_JAR}")
            sys.exit(1)
        generateAntlr2Python()
    elif argv[0] == 'test':
        if len(argv) < 2:
            printUsage()
        elif argv[1] == 'py':
            filename = argv[2] if len(argv) > 2 else '001.txt'
            runPythonTest(filename)
        elif argv[1] == 'java':
            filename = argv[2] if len(argv) > 2 else '002.txt'
            runJavaTest(filename)
        elif argv[1] == 'command':
            filename = argv[2] if len(argv) > 2 else '003.txt'
            runCommandTest(filename)
        else:
            printUsage()
    else:
        printUsage()

if __name__ == '__main__':
    main(sys.argv[1:])