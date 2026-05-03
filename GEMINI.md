# JavaPy-Translator

## Project Overview
This project is a bidirectional code translation framework that converts code between Java and Python using formal language theory principles. It features a React-based frontend providing a ChatGPT-like interactive interface, and a FastAPI-based backend that uses ANTLR4 grammars for parsing and translation. 

Key Components:
- **Backend**: FastAPI server, ANTLR4 grammars (`.g4` files) for Java and Python, and custom Visitor classes that parse abstract syntax trees (AST) to generate target code.
- **Frontend**: React.js application using Vite and Tailwind CSS, communicating with the backend via RESTful APIs.

## Building and Running

### Prerequisites
- Python 3.8+
- Node.js 16+
- Java JDK 8+ (required for regenerating ANTLR parsers)

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Install Python dependencies:
   ```bash
   pip install fastapi uvicorn antlr4-python3-runtime python-multipart
   ```
3. Start the FastAPI server:
   ```bash
   uvicorn server:app --reload
   ```
   The backend will run at `http://localhost:8000`.

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install Node dependencies:
   ```bash
   npm install
   ```
3. Start the Vite development server:
   ```bash
   npm run dev
   ```
   The frontend will run at `http://localhost:5173`.

### ANTLR Grammar Regeneration
If you modify any of the `.g4` files in the `backend` directory, you need to regenerate the parsers:
```bash
cd backend
antlr4 -Dlanguage=Python3 -visitor py2java.g4
antlr4 -Dlanguage=Python3 -visitor java2py.g4
antlr4 -Dlanguage=Python3 -visitor command.g4
```
*(Assumes `antlr4` alias is configured correctly on your system).*

## Development Conventions

- **Grammar Changes**: The core parsing logic lives in the ANTLR `.g4` files. Any language feature additions or syntax changes must start here.
- **Translation Logic**: The Visitor Pattern is used to traverse the AST. Translation logic is implemented in `backend/py2javaVisitor.py`, `backend/java2pyVisitor.py`, and `backend/commandVisitor.py`. Type inference and symbol management are handled within these visitors.
- **Frontend Architecture**: Built using React functional components and hooks (`useState`, `useEffect`). UI styling uses Tailwind CSS. API interactions are modularized in `frontend/src/services/api.js`.
- **Command Processing**: A dedicated ANTLR grammar (`command.g4`) allows natural language commands in the chat interface like "show tree" or "translate python to java".

## Testing
- **Backend Testing**: `python -m pytest tests/` inside the `backend/` directory.
- **Frontend Testing**: `npm test` inside the `frontend/` directory.
