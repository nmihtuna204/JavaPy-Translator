# Supported Syntax for JavaPy-Translator

## Python to Java Conversion

### ✅ Supported Python Syntax

#### Basic Statements
- `def functionName(): ...` - Function definition
- `return value` - Return statement
- `break` - Break statement
- `print(args)` - Print statement
- Function calls: `functionName()`

#### Control Flow
- `if condition: ...` - If statement
- `elif condition: ...` - Elif statement (multiple)
- `else: ...` - Else block
- `while condition: ...` - While loop
- `for var in range(start, stop, step): ...` - For loop

#### Expressions & Operators
- **Arithmetic**: `+`, `-`, `*`, `/`
- **Comparison**: `>`, `<`, `==`, `!=`, `<=`, `>=`
- **Logical**: `and`, `or`, `not`
- **Unary**: `-value`
- **Assignment**: `var = value`
- **Increment/Decrement**: `var++`, `var--`, `var+=`, `var-=`

#### Data Types
- Numbers: `123`, `45.67`
- Strings: `"hello"`, `'world'`
- Booleans: `True`, `False`
- None: `None`

#### Special
- `if __name__ == "__main__": ...` - Main block

### ❌ NOT Supported
- ❌ `from x import y` - Import statements
- ❌ `@decorator` - Decorators
- ❌ `app.method()` - Method calls with dot notation
- ❌ `ClassName()` - Class instantiation
- ❌ List/Dict/Set comprehensions
- ❌ Lambda functions
- ❌ Try/Except blocks
- ❌ With statements
- ❌ Class definitions
- ❌ Comments
- ❌ Multiple assignments

---

## Java to Python Conversion

### ✅ Supported Java Syntax

#### Basic Statements
- `public static void main(String[] args) { ... }` - Main method
- `System.out.println(args)` - Print statement
- `return value;` - Return statement
- `break;` - Break statement
- Method calls: `methodName()`

#### Control Flow
- `if (condition) { ... }` - If statement
- `else if (condition) { ... }` - Else if statement
- `else { ... }` - Else block
- `while (condition) { ... }` - While loop
- `for (init; condition; update) { ... }` - For loop

#### Expressions & Operators
- **Arithmetic**: `+`, `-`, `*`, `/`, `%`
- **Comparison**: `>`, `<`, `==`, `!=`, `<=`, `>=`
- **Logical**: `&&`, `||`, `!`
- **Assignment**: `var = value;`
- **Increment/Decrement**: `var++`, `var--`, `var+=`, `var-=`

#### Data Types
- Numbers: `int`, `double`, `long`
- Strings: `String "text"`
- Booleans: `true`, `false`
- Null: `null`

### ❌ NOT Supported
- ❌ `import` statements
- ❌ Class definitions (except main class)
- ❌ Methods (except main)
- ❌ Annotations
- ❌ Try/Catch blocks
- ❌ Generics
- ❌ Lambda expressions
- ❌ Inner classes
- ❌ Comments

---

## Conversion Quality

⚠️ **Important Notes:**
- Conversion is **syntax-based only** (ANTLR grammar parsing)
- No semantic analysis or logic optimization
- Complex Python features won't convert
- Output may need manual adjustment
