# JavaPy-Translator

## Project Overview
JavaPy-Translator is a bidirectional code translator that converts Java to Python and vice versa. The project features a chat-style user interface where users can type code or natural language commands, with results streaming back in a conversation view. It uses ANTLR4 for parsing, a FastAPI backend for handling translations, and a React + Vite + Tailwind frontend for the user interface. It was created for a Principles of Programming Languages (PPL) course.

### Main Technologies
- **Backend:** Python (FastAPI, Uvicorn, Pydantic), ANTLR4 (with Java 8+ required for regenerating grammars or running Java code)
- **Frontend:** React, Vite, Tailwind CSS

### Architecture
- **backend/**: Contains the FastAPI server (`server.py`) with a single `POST /convert` endpoint. Contains ANTLR grammars (`.g4`), translation logic (visitors), and a CLI tool (`run.py`) for code generation and testing.
- **frontend/**: Contains a React application that persists multiple conversations in `localStorage` and communicates with the backend via `fetch` requests. 

## Building and Running

Two terminals are required to run this project: one for the backend and one for the frontend.

### Backend Setup & Execution
1. Navigate to the `backend/` directory: `cd backend`
2. Create and activate a Python virtual environment:
   - macOS/Linux: `python3 -m venv .venv && source .venv/bin/activate`
   - Windows: `python -m venv .venv` and `.venv\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Start the server: `uvicorn server:app --reload`
   - The backend runs on `http://localhost:8000`. Swagger docs are at `/docs`.

*Note: A Java JDK 8+ is required to execute translated Java code (via `javac` and `java`) or to regenerate ANTLR grammars.*

### Frontend Setup & Execution
1. Navigate to the `frontend/` directory: `cd frontend`
2. Install dependencies: `npm install`
3. Start the development server: `npm run dev`
   - The frontend runs on `http://localhost:5173`.

### Regenerating Grammars & Testing (Backend)
- To regenerate ANTLR parsers (requires Java JDK): `python run.py gen`
- To run Python to Java tests: `python run.py test py`

## Development Conventions
- The application uses `localStorage` in the browser to maintain separate chat sessions.
- The UI handles switching between code editing and chat commands. Chat commands like `translate python to java`, `show grammar`, and `show output` act as control instructions for the backend.
- The grammar configurations reside in `backend/grammars/`, and visitor logic implementation resides in `backend/logic/`. Ensure any modifications to `.g4` files are followed by parser regeneration.
- Do not commit changes to `.venv` or `node_modules` folders. Keep UI changes within the component-based architecture described in `frontend/src/`.
