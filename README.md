# Python-to-Java Code Converter

A sophisticated web-based application that converts Python code to Java using ANTLR parsing technology, featuring a ChatGPT-like interface for seamless code translation and interaction.

## 🚀 Features

- **Bidirectional Code Translation**: Convert Python to Java and Java to Python
- **Interactive Chat Interface**: Natural language commands for code interaction
- **Real-time Code Execution**: View output of executed Python code
- **Parse Tree Visualization**: Display grammar and parse trees
- **Code Management**: Save, store, and retrieve code snippets
- **Modern UI**: React-based frontend with Tailwind CSS styling

## 🏗️ Project Architecture

```
Project for theory class/
├── backend/                 # FastAPI backend with ANTLR parsing
│   ├── server.py           # Main FastAPI server
│   ├── py2java.g4          # Python to Java ANTLR grammar
│   ├── java2py.g4          # Java to Python ANTLR grammar
│   ├── command.g4          # Command parsing grammar
│   ├── py2javaVisitor.py   # Python to Java conversion logic
│   ├── java2pyVisitor.py   # Java to Python conversion logic
│   ├── commandVisitor.py   # Command parsing visitor
│   └── CompiledFiles/      # Generated ANTLR parser files
├── frontend/               # React frontend application
│   ├── src/               # React source code
│   ├── package.json       # Node.js dependencies
│   └── vite.config.js     # Vite configuration
└── README.md              # This file
```

## 📋 Prerequisites

Before setting up this project, ensure you have the following installed:

### Required Software:
- **Python 3.8+** ([Download Python](https://www.python.org/downloads/))
- **Node.js 16+** and **npm** ([Download Node.js](https://nodejs.org/))
- **Java JDK 8+** (for ANTLR, if regenerating parsers)

### ANTLR Setup (Required for Grammar Regeneration):
1. **Create ANTLR directory:**
   ```bash
   # Windows
   mkdir C:\antlr
   
   # macOS/Linux
   mkdir /usr/local/lib/antlr
   ```

2. **Download ANTLR JAR file:**
   - Download `antlr4-4.9.2-complete.jar` from: https://www.antlr.org/download/antlr-4.9.2-complete.jar
   - **Windows**: Place it in `C:\antlr\antlr4-4.9.2-complete.jar`
   - **macOS/Linux**: Place it in `/usr/local/lib/antlr/antlr4-4.9.2-complete.jar`

3. **Set up ANTLR alias (Optional but recommended):**
   
   **Windows (PowerShell):**
   ```powershell
   # Add to your PowerShell profile
   function antlr4 { java -jar C:\antlr\antlr4-4.9.2-complete.jar $args }
   ```
   
   **macOS/Linux (Bash/Zsh):**
   ```bash
   # Add to your ~/.bashrc or ~/.zshrc
   alias antlr4='java -jar /usr/local/lib/antlr/antlr4-4.9.2-complete.jar'
   export CLASSPATH=".:/usr/local/lib/antlr/antlr4-4.9.2-complete.jar:$CLASSPATH"
   ```

### Verify Installation:
```bash
python --version    # Should show Python 3.8+
node --version      # Should show Node 16+
npm --version       # Should show npm version
java --version      # Should show Java version
antlr4              # Should show ANTLR help (if alias is set up)
```

## 🛠️ Installation & Setup

### Step 1: Clone the Repository
```bash
git clone <your-repository-url>
cd "Project for theory class"
```

### Step 2: Backend Setup (FastAPI)

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Install Python dependencies:**
   ```bash
   pip install fastapi uvicorn antlr4-python3-runtime python-multipart
   ```
   
   *Or if you have a requirements.txt:*
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify backend setup:**
   ```bash
   python -c "import fastapi, uvicorn, antlr4; print('Backend dependencies installed successfully!')"
   ```

4. **Start the backend server:**
   ```bash
   uvicorn server:app --reload
   ```
   
   **Expected output:**
   ```
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   INFO:     Started reloader process
   ```

   ✅ Backend is now running at `http://localhost:8000`

### Step 3: Frontend Setup (React)

1. **Open a new terminal and navigate to frontend:**
   ```bash
   cd frontend
   ```

2. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm run dev
   ```
   
   **Expected output:**
   ```
   VITE v4.x.x  ready in xxx ms
   
   ➜  Local:   http://localhost:5173/
   ➜  Network: use --host to expose
   ```

   ✅ Frontend is now running at `http://localhost:5173`

## 🎯 Usage Guide

### Quick Start:
1. Ensure both backend and frontend servers are running
2. Open your browser and go to `http://localhost:5173`
3. You should see a chat interface

### Example Usage:

#### 1. Basic Python to Java Conversion:
```
Input: print("Hello, World!")
Output: System.out.println("Hello, World!");
```

#### 2. Available Commands:
- `show grammar` - Display the parse tree/grammar
- `show output` - Show the output of executed Python code
- `store code` or `save code` - Save the current code
- `retrieve saved code` or `get saved code` - Load previously saved code
- `translate python to java` - Switch to Python→Java mode
- `translate java to python` - Switch to Java→Python mode

#### 3. Sample Conversation:
```
You: x = 5
Bot: int x = 5;

You: show output
Bot: [Shows execution result]

You: save code
Bot: Code saved successfully!
```

## 🔧 Troubleshooting

### Common Issues:

#### Backend Issues:
- **Port 8000 already in use:**
  ```bash
  uvicorn server:app --reload --port 8001
  ```

- **Missing dependencies:**
  ```bash
  pip install fastapi uvicorn antlr4-python3-runtime python-multipart
  ```

- **ANTLR import errors:**
  - Ensure `CompiledFiles/` directory exists with generated parser files
  - If missing, the project should still work with basic functionality

#### Frontend Issues:
- **Port 5173 already in use:**
  ```bash
  npm run dev -- --port 3000
  ```

- **npm install fails:**
  ```bash
  rm -rf node_modules package-lock.json
  npm cache clean --force
npm install
  ```

- **Build errors:**
  ```bash
  npm run build
  ```

#### Connection Issues:
- **Frontend can't reach backend:**
  - Verify backend is running on `http://localhost:8000`
  - Check browser console for CORS errors
  - Ensure no firewall blocking local connections

### Verification Steps:
1. **Test backend API directly:**
   ```bash
   curl http://localhost:8000/health
   ```

2. **Check frontend build:**
   ```bash
   npm run build
   ```

## 🧪 Testing

### Backend Testing:
```bash
cd backend
python -m pytest tests/
```

### Frontend Testing:
```bash
cd frontend
npm test
```

## 🔄 Development Workflow

### Making Changes:
1. **Backend changes**: Server auto-reloads with `--reload` flag
2. **Frontend changes**: Vite hot-reloads automatically
3. **Grammar changes**: Regenerate ANTLR files if modifying `.g4` files

### ANTLR Grammar Regeneration (Advanced):
If you modify the grammar files, regenerate parsers:

**Using ANTLR JAR directly:**
```bash
cd backend

# Windows
java -jar C:\antlr\antlr4-4.9.2-complete.jar -Dlanguage=Python3 -visitor py2java.g4
java -jar C:\antlr\antlr4-4.9.2-complete.jar -Dlanguage=Python3 -visitor java2py.g4
java -jar C:\antlr\antlr4-4.9.2-complete.jar -Dlanguage=Python3 -visitor command.g4

# macOS/Linux
java -jar /usr/local/lib/antlr/antlr4-4.9.2-complete.jar -Dlanguage=Python3 -visitor py2java.g4
java -jar /usr/local/lib/antlr/antlr4-4.9.2-complete.jar -Dlanguage=Python3 -visitor java2py.g4
java -jar /usr/local/lib/antlr/antlr4-4.9.2-complete.jar -Dlanguage=Python3 -visitor command.g4
```

**Using alias (if set up):**
```bash
cd backend
antlr4 -Dlanguage=Python3 -visitor py2java.g4
antlr4 -Dlanguage=Python3 -visitor java2py.g4
antlr4 -Dlanguage=Python3 -visitor command.g4
```

**Important Notes:**
- The ANTLR JAR file is **required** only if you plan to modify the grammar files (`.g4` files)
- For normal usage of the application, the pre-generated parser files in `CompiledFiles/` are sufficient
- If `CompiledFiles/` directory is missing or corrupted, you'll need ANTLR to regenerate the parsers

## 📚 API Documentation

Once the backend is running, visit:
- **Interactive API docs**: `http://localhost:8000/docs`
- **ReDoc documentation**: `http://localhost:8000/redoc`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a Pull Request

## 📄 License

This project is created for educational purposes as part of a Principles of Programming Languages course.

## 📞 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Verify all prerequisites are installed
3. Ensure both servers are running simultaneously
4. Check browser console for error messages

---

**Happy coding! 🚀**

*For questions about the implementation, please refer to the code comments or contact the project maintainer.*
