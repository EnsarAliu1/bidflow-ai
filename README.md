# BidFlow AI

Backend built with Python and FastAPI.

## Requirements

- Python 3.10 or newer
- Bash terminal (Git Bash on Windows)

## Run the backend

From the project root:

```bash
cd backend
python -m venv .venv
```

Activate the virtual environment with the command for your system.

**Git Bash on Windows:**

```bash
source .venv/Scripts/activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

Install the backend and its dependencies from `pyproject.toml`:

```bash
python -m pip install -e .
```

Start the development server:

```bash
python -m uvicorn app.main:app --reload
```

- Backend: http://127.0.0.1:8000
- API documentation: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/api/v1/health

Expected health check response:

```json
{
  "status": "ok",
  "service": "bidflow-api"
}
```

Press `Ctrl+C` to stop the server.
