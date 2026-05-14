# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

### Backend

```bash
cd backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn server:app --reload          # runs at http://localhost:8000
```

Regenerate ANTLR parsers after editing any `.g4` file:
```bash
python run.py gen
```

Run grammar smoke tests against sample inputs in `backend/tests/`:
```bash
python run.py test py                 # Python→Java on tests/001.txt
python run.py test py 001.txt         # specific file
python run.py test java 002.txt       # Java→Python
python run.py test command 003.txt    # command grammar
```

Quick API smoke test:
```bash
curl -X POST http://localhost:8000/convert \
  -H "Content-Type: application/json" \
  -d '{"code":"def hello():\n    print(\"Hi\")\n", "conversation_id":"smoke"}'
```

### Frontend

```bash
cd frontend
npm install
npm run dev      # runs at http://localhost:5173
npm run lint
npm run build
```

### Docker (backend only)

```bash
docker-compose up --build
```

## Architecture

This is a bidirectional Java ↔ Python translator with a chat-style UI. The two sides are completely independent — backend is pure Python/ANTLR, frontend is React/Vite.

### Backend (`backend/`)

**Translation pipeline** — for each request to `POST /convert`:
1. The input is first tried against the **command grammar** (`grammars/command.g4`, compiled into `CompiledFiles/`). The `commandVisitor` returns a string token (`"pytojava"`, `"javatopy"`, `"showgrammar"`, `"showoutput"`, `"savecode"`, `"showsavedcode"`, or `"0"` for non-command).
2. If the result is `"0"` (not a command), the input is routed to a code translator based on the per-conversation `direction`. Direction is auto-detected from heuristics if not yet set.
3. Code translation runs ANTLR parse (using one of `py2javaLexer/Parser` or `java2pyLexer/Parser`) then a visitor (`logic/py2javaVisitor.py` or `logic/java2pyVisitor.py`) that walks the CST and emits the target language string.

**Key files:**
- `server.py` — FastAPI app, all endpoint logic, in-memory conversation state (`conversation_contexts` dict keyed by `conversation_id`)
- `grammars/*.g4` — ANTLR source grammars (edit these, then run `python run.py gen`)
- `CompiledFiles/` — ANTLR-generated lexers/parsers/base visitors (committed; do not hand-edit)
- `logic/py2javaVisitor.py` — CST visitor that emits Java from Python parse tree
- `logic/java2pyVisitor.py` — CST visitor that emits Python from Java parse tree
- `logic/commandVisitor.py` — interprets chat commands
- `logic/tree_printer_py.py`, `logic/tree_printer_java.py` — pretty-print parse trees for `show grammar`

**Conversation state** is in-memory only (lost on server restart). Each conversation tracks: `last_code`, `last_tree`, `saved_code`, `saved_tree`, `direction`.

**Code execution:** Python runs via `exec()` in-process. Java is written to a temp file, compiled with `javac`, and run with `java` (10 s timeout). Both require `javac`/`java` on `PATH` for Java execution.

### Frontend (`frontend/`)

React 18 + Vite + Tailwind. Single-page chat UI. Each conversation has its own `conversation_id` (generated client-side) stored in `localStorage`. The frontend service layer (`services/api.js`) calls `POST /convert` on the backend — if the backend port changes from `8000`, update that file.

### Grammar regeneration

Editing a `.g4` requires regenerating the Python parser. The ANTLR jar is vendored at `backend/antlr_jar/antlr4-4.9.2-complete.jar`. Use `python run.py gen` or run `java -jar` manually (see `backend/README.md`). The generated `CompiledFiles/` are committed.
