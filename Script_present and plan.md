# Presentation Script: JavaPy-Translator (~6 mins)

## Preparation
- **Tab 1**: `landing.html` open at `#team`.
- **Tab 2**: The live application, already loaded.
- Rehearse the demo inputs so there is no typing delay.

---

## 1. Team & Vision — Lê Hưng (1:15)
**Action**: Stay on `landing.html` → `#team`.

> "Good morning. We are the team behind **JavaPy-Translator** — a bidirectional compiler-middleware that translates between Java and Python using formal language theory.
>
> I am **Lê Hưng**, the team lead. I designed the FastAPI backend and the conversation model at its core. The key architectural insight is this: rather than treating every request as an isolated conversion, we model each browser chat session as a **stateful compilation unit**. The server keeps a per-conversation context — last code, last parse tree, saved snapshot, and translation direction. This lets users chain commands — translate, inspect the tree, run the output, save the code — all within the same session, exactly like interacting with a compiler REPL.
>
> The translation pipeline has three layers: an ANTLR **lexer** tokenizes the input, a **parser** builds a Concrete Syntax Tree, and a **visitor** walks that tree to emit the target language. We implemented *three* separate ANTLR grammars — one for Python→Java, one for Java→Python, and one for a natural-language command DSL. Let my teammates walk you through each layer."

---

## 2. Grammar Architecture — Nguyễn Minh Phúc (1:45)
**Action**: Click **'Grammar Design'** on `landing.html`.

> "I am **Nguyễn Minh Phúc**, the Grammar Architect. I wrote all three ANTLR4 Context-Free Grammars. Let me highlight the three problems I had to solve.
>
> **First: structural asymmetry.** Java is brace-delimited — `classDef → classBody → methodDef → block`. Python is indentation-delimited. These are fundamentally different block models. For Python, I could not just skip whitespace. I had to make the `NL` lexer rule *capture* the newline and any following tabs, so the parser can use indentation to identify block boundaries. On the Java side, `NL` is discarded entirely — `NL: ... -> skip`.
>
> **Second: operator precedence.** Both grammars encode PEMDAS directly in the rule hierarchy — from `logicExp` at the top, down through `compExp`, `addExp`, `mulExp`, to `unaryExp` and finally `atom`. Because `mulExp` is deeper in the tree than `addExp`, multiplication is parsed first, without a single explicit precedence annotation.
>
> **Third: the Command DSL.** Instead of a separate UI for switching modes, I defined a third grammar that recognizes natural language phrases: `verb noun* target?`. A word like `translate` becomes a `verb`, `python` and `java` become `source` and `target_lang`. The server tries the command grammar first on *every* request. If the visitor returns `'0'` — not a command — the input falls through to the code translator. This means one endpoint handles everything."

---

## 3. Visitor Logic & Type Inference — Nguyễn Minh Tuấn (1:15)
**Action**: Click **'Mapping Logic'** on `landing.html`.

> "I am **Nguyễn Minh Tuấn**. I implemented the two Visitor classes that walk the parse tree and emit code.
>
> The Visitor Pattern is the right fit here because it keeps translation logic entirely separate from the grammar. Each `visitX` method handles exactly one grammar rule.
>
> The hardest problem was **type inference for Python→Java**. Python is dynamically typed, so `x = 5` has no type annotation. My `inferType` method walks the expression's subtree bottom-up: if it reaches an `AtomContext` and finds a `FLOAT` token, it returns `double`; a `STRING` token returns `String`; `TRUE`/`FALSE` returns `boolean`; otherwise `int`. Logical and comparison operators short-circuit to `boolean`. This runs at parse time — no separate analysis pass needed.
>
> The other challenge was **loop translation**. Python's `for i in range(start, stop, step)` maps to Java's triple-header `for (int i = start; i < stop; i += step)`. In the reverse direction, Java's C-style for loop has no direct Python equivalent, so my Java→Python visitor converts it into a `while` loop with explicit initialization and increment statements.
>
> Indentation in Java→Python is managed by an `indent_level` counter that increments on block entry and decrements on exit — producing correct Python whitespace structurally, not by string replacement."

---

## 4. Live Demo & Closing — Lê Nhật Anh (1:30)
**Action**: Switch to the **Live App Tab**.

> "I am **Lê Nhật Anh**, the Frontend Developer. I built the chat UI in React 18 + Vite + Tailwind. Each conversation is fully independent — its own ID, its own direction, its own saved code, all persisted in `localStorage` so sessions survive page refreshes.
>
> **[Action: In a new conversation, type:]**
> ```
> translate python to java
> ```
> The server's command grammar picks this up and returns direction `pytojava`.
>
> **[Action: Paste and send:]**
> ```python
> def factorial(n):
>     if n <= 1:
>         return 1
>     return n * factorial(n - 1)
>
> if __name__ == "__main__":
>     print(factorial(5))
> ```
> The parse tree is built, the visitor walks it, and we get idiomatic Java — with static typing, curly braces, and `System.out.println`.
>
> **[Action: Send `show grammar`]**
> This retrieves the stored parse tree from the server and renders the ANTLR node hierarchy Phúc designed.
>
> **[Action: Send `show output`]**
> The server compiles the Java with `javac`, runs it with `java`, captures stdout, and returns `120`.
>
> In six minutes we have shown a complete PPL pipeline: formal grammars, LL(*) parsing, visitor-based code generation, and type inference — all integrated into a live, stateful chat application. Thank you."

---

## Timing Summary

| Speaker | Section | Target |
|---|---|---|
| Lê Hưng | Team & Vision | 1:15 |
| Nguyễn Minh Phúc | Grammar Architecture | 1:45 |
| Nguyễn Minh Tuấn | Visitor Logic & Type Inference | 1:15 |
| Lê Nhật Anh | Live Demo & Closing | 1:30 |
| **Total** | | **~5:45** |
