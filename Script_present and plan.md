# Detailed Presentation Script: JavaPy-Translator (5 Mins)

## Preparation
- **Tab 1**: `landing.html` (Primary visual aid).
- **Tab 2**: The live application (Demo environment).

---

## 1. Team & Vision (Lê Hưng - 1:00)
**Action**: Stay on `landing.html#team`.
> "Good morning. We are the team behind **JavaPy-Translator**. Manual code migration is a bottleneck in modern development; our project applies formal language theory to automate bidirectional translation between Java and Python.
>
> I am **Lê Hưng**, the Team Lead. I architected the FastAPI backend and Docker orchestration. Our vision was to create more than a converter—we built a compiler-middleware that treats 'conversations' as distinct compilation units. As we walk through the technical stack, keep in mind that our goal was semantic preservation: ensuring that logic, not just text, survives the translation."

---

## 2. Grammar Architecture (Nguyễn Minh Phúc - 2:00)
**Action**: Click 'Grammar Design' on `landing.html`.
> "My name is **Nguyễn Minh Phúc**, and I am the Grammar Architect. The foundation of this system is its **Context-Free Grammars**. 
>
> As shown on the left, we designed a **Recursive Descent Hierarchy**. For Java, we strictly follow class and method definitions. For Python, we had to solve a unique Lexical challenge: **Indentation**. Look at our `NL` lexer rule—it captures newlines and following spaces to preserve the block structure, which the parser then uses to identify scopes.
>
> On the right, notice our **Expression Hierarchy**. This is where we apply PPL principles for **Operator Precedence**. By nesting rules from `logicExp` down to `mulExp` and `unaryExp`, we enforce PEMDAS rules directly within the syntax tree. This means the parser 'knows' multiplication has higher precedence than addition before any logic is even executed. We also implemented a **Command DSL** that allows natural language control over the engine."

---

## 3. Mapping Logic (Nguyễn Minh Tuấn - 1:00)
**Action**: Click 'Mapping Logic' on `landing.html`.
> "I am **Nguyễn Minh Tuấn**, responsible for the Visitor implementation. Once Phúc's grammar creates the Parse Tree, my logic 'walks' it.
>
> The most critical challenge I solved was **Type Inference**. Since Python is dynamically typed, my engine must analyze literals—like `5.0` vs `"5"`—to decide if the Java equivalent should be a `double` or a `String`. We also map complex constructs: for instance, transforming a Python `range()` into a standard Java triple-header for-loop. This isn't just translation; it's a semantic bridge between two fundamentally different type systems."

---

## 4. Live Demo & Closing (Lê Nhật Anh - 1:00)
**Action**: Switch to the **Live App Tab**.
> "I am **Lê Nhật Anh**, the Frontend Developer. I built the interface using React and Vite, with a focus on persistence. 
> 
> Let's see the system in action. I'll type a Python loop... [Action: Translate code]. The result is idiomatic Java. Now, watch as we inspect the **Parse Tree** using the 'show grammar' command [Action: Show tree]. This visualizes the rules Phuc just explained. Finally, we can execute the code directly [Action: Show output] to verify its behavior.
>
> JavaPy-Translator proves that formal PPL concepts are the key to building intelligent, cross-language developer tools. Thank you!"
