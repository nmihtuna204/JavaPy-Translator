# Frontend — JavaPy-Translator

React + Vite + Tailwind CSS chat UI for the JavaPy-Translator. Talks to the FastAPI backend via `POST /convert`.

---

## Layout

```
frontend/
├── index.html
├── vite.config.js
├── tailwind.config.js
├── postcss.config.js
├── eslint.config.js
├── package.json
├── services/
│   └── api.js              # convertCode() — fetch wrapper around POST /convert
├── utils/
│   └── helpers.js          # ID generation, localStorage helpers, etc.
└── src/
    ├── main.jsx            # React entry point
    ├── App.jsx             # Root component (chat layout + state)
    ├── App.css / index.css / global.css
    ├── components/
    │   ├── Sidebar.jsx     # Conversation list (persisted in localStorage)
    │   └── ThemeToggle.jsx # Light/dark mode switch
    └── contexts/           # React contexts (e.g. theme)
```

---

## Prerequisites

- **Node.js 16+** and **npm**
- The backend running at `http://localhost:8000` (see [`../backend/README.md`](../backend/README.md)).

---

## Setup & run

From the `frontend/` directory:

```bash
cd frontend
npm install
npm run dev
```

The dev server starts at `http://localhost:5173`. Vite hot-reloads on save.

If the port is taken:
```bash
npm run dev -- --port 3000
```

### Other scripts

```bash
npm run build      # Production build into dist/
npm run preview    # Serve the production build locally
npm run lint       # Run ESLint
```

---

## Backend URL

The frontend talks to the backend through `services/api.js`:

```js
const res = await fetch('http://localhost:8000/convert', { ... });
```

If you run the backend on a different host/port, edit that URL.

---

## How the UI is wired

- **`App.jsx`** holds the conversation list and the active conversation, sends user input to `convertCode()`, and appends both the user message and the bot reply to the active conversation.
- **`Sidebar.jsx`** lists all conversations from `localStorage`; clicking switches the active conversation; "New" creates a fresh one.
- **`ThemeToggle.jsx`** flips between light and dark via a React context; the choice is persisted.
- **`services/api.js`** normalizes the backend response (`result`, `type`, `message`, `direction`) and turns network errors into user-visible messages.

Each conversation keeps its own `direction` (Python → Java or Java → Python) and saved code on the backend, keyed by `conversation_id`. The frontend just forwards that ID with every request.

---

## Common issues

- **"Could not connect to the server"** — confirm the backend is running at `http://localhost:8000` and CORS isn't blocking it (it shouldn't — the backend allows all origins).
- **Blank page after `npm run dev`** — check the browser console; usually a missing dependency. Try:
  ```bash
  rm -rf node_modules package-lock.json
  npm install
  ```
- **Tailwind classes not applying** — make sure `tailwind.config.js` and `postcss.config.js` weren't accidentally edited; restart the dev server after changes.

---

## Tech stack

- **React 18** with hooks
- **Vite 5** for dev server + bundling
- **Tailwind CSS 3** for styling
- **ESLint** with React plugins for linting
