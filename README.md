# BidFlow AI

Backend built with Python and FastAPI.

## Run the backend

From the project root, run in Bash:

```bash
cd backend
python -m venv .venv
```

Activate the virtual environment using the command for your system:

```bash
# Git Bash on Windows
source .venv/Scripts/activate

# Linux / macOS
source .venv/bin/activate
```

Install dependencies and start the server:

```bash
python -m pip install fastapi "uvicorn[standard]"
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
