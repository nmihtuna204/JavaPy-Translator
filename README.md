# JavaPy-Translator

A bidirectional **Java ↔ Python** code translator built on ANTLR4, served by a FastAPI backend with a React + Vite chat-style frontend. Created for the **Principles of Programming Languages (PPL)** course.

---

## Highlights

- **Bidirectional translation**: Python → Java and Java → Python.
- **Chat-style UI**: type code or natural-language commands; results stream into a conversation.
- **Multi-conversation**: each session has its own translation direction and saved code (persisted in `localStorage`).
- **Code execution**: run the translated Python (`exec`) or Java (`javac` + `java`) and see the output.
- **Parse-tree view**: visualize the ANTLR parse tree for any input.
- **Light / dark theme** toggle.

---

## Repository layout

```
JavaPy-Translator/
├── backend/                  # FastAPI + ANTLR4 translation engine
├── frontend/                 # React + Vite + Tailwind chat UI
├── README.md                 # This file (overview)
├── Project_Documentation.md  # Detailed PPL framework documentation
├── SUPPORTED_SYNTAX.md       # What the grammars currently accept
└── TEST_CASES.md             # Ready-to-run test cases
```

Each side has its own setup guide:
- **Backend** → see [`backend/README.md`](backend/README.md) (covers `.venv` and local Python setups).
- **Frontend** → see [`frontend/README.md`](frontend/README.md).

---

## Quick start

You need **two terminals**: one for the backend, one for the frontend.

### 1. Start the backend

```bash
cd backend
python -m venv .venv && source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate                            # Windows
pip install -r requirements.txt
uvicorn server:app --reload
```

Backend runs at `http://localhost:8000` (Swagger UI at `/docs`).

### 2. Start the frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at `http://localhost:5173`.

Open the URL in your browser, paste some code, and start translating.

---

## Prerequisites

| Tool        | Version  | Used for                                          |
|-------------|----------|---------------------------------------------------|
| Python      | 3.8+     | Backend runtime                                   |
| Node.js     | 16+      | Frontend dev server                               |
| Java JDK    | 8+       | Running translated Java code; regenerating ANTLR  |
| ANTLR jar   | 4.9.2    | Already vendored at `backend/antlr_jar/`          |

The pre-generated parsers in `backend/CompiledFiles/` are committed, so you only need ANTLR if you change a `.g4` file.

---

## Available chat commands

Inside the chat box you can type either code or one of:

| Command                              | Action                                       |
|--------------------------------------|----------------------------------------------|
| `translate python to java`           | Set this conversation to Python → Java       |
| `translate java to python`           | Set this conversation to Java → Python       |
| `show grammar`                       | Display the parse tree of the last input     |
| `show output`                        | Run the last code and show its output        |
| `save code` / `store code`           | Save current code in this conversation       |
| `show saved code` / `get saved code` | Restore the saved code                       |

If no direction is set, the backend auto-detects the language from the code.

---

## Documentation

- [`Project_Documentation.md`](Project_Documentation.md) — full architectural and PPL framework write-up.
- [`SUPPORTED_SYNTAX.md`](SUPPORTED_SYNTAX.md) — currently supported syntax for both directions.
- [`TEST_CASES.md`](TEST_CASES.md) — ready-to-paste test inputs with expected outputs.

---

## License

Created for educational purposes as part of a Principles of Programming Languages course.