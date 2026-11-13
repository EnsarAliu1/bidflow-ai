# BidFlow AI

Tender management application with a Python/FastAPI backend and a Next.js frontend.

## Requirements

- Python 3.10 or newer
- Bash terminal (Git Bash on Windows)
- Docker with Docker Compose (Docker Desktop on Windows)
- Node.js 20.9 or newer and npm (for the frontend)

## Database setup

Start Docker Desktop, then run these commands from the project root. Copy the
environment template only if you do not already have a `.env` file:

```bash
cp -n .env.example .env
```

Edit the project-root `.env` with your local database credentials:

```dotenv
POSTGRES_DB=bidflow
POSTGRES_USER=bidflow
POSTGRES_PASSWORD=replace_with_a_local_password
POSTGRES_HOST=127.0.0.1
POSTGRES_PORT=5432
```

Both Docker Compose and the backend read this file. Start PostgreSQL 16:

```bash
docker compose up -d db
docker compose ps
```

Wait for `db` to show as healthy. PostgreSQL is exposed at `127.0.0.1:5432`
and stores data in the `postgres_data` Docker volume. Credentials initialize
the database on its first startup; changing `.env` later does not change an
existing database user's password.

To inspect startup problems or stop the database while retaining its data:

```bash
docker compose logs db
docker compose stop db
```

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

Apply the existing migrations before starting the development server
(keep PostgreSQL running):

```bash
python -m alembic upgrade head
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

## Frontend setup

Keep PostgreSQL and the backend running as described above. In a separate
terminal, start from the project root:

```bash
cd frontend
npm ci
```

Create `frontend/.env.local` from the included template only if you do not
already have this file:

```bash
cp -n .env.example .env.local
```

For PowerShell, use this command instead:

```powershell
if (!(Test-Path .env.local)) { Copy-Item .env.example .env.local }
```

The frontend environment file should contain:

```dotenv
API_BASE_URL=http://127.0.0.1:8000/api/v1
```

Include `/api/v1` and omit the trailing slash: the API client appends `/tenders`.
This variable is read on the server; it does not need a `NEXT_PUBLIC_` prefix.
The frontend uses its own `.env.local`, separate from the project-root database
`.env`. Restart the frontend development server after changing its environment.

Start the frontend:

```bash
npm run dev
```

Open http://localhost:3000 (or the URL printed in the terminal). The dashboard
loads tender statistics and the tender table from the backend. An empty database
shows zero counts and "No tenders yet"; a failed API request shows an error state.

If tenders cannot load, check that PostgreSQL and the backend are running, that
migrations have been applied, and that http://127.0.0.1:8000/api/v1/tenders returns
a JSON array. Then retry in the dashboard.

Available checks and production commands, run from `frontend/`:

```bash
npm run lint
npm run build
npm run start
```

`npm run start` serves the production build after `npm run build` completes.
Keep the backend available when running the application. Press `Ctrl+C` in the
frontend terminal to stop its server.

## Database migrations

Run Alembic commands from `backend/` with the virtual environment activated
and PostgreSQL running. Alembic uses the database settings in the project-root
`.env`.

For a fresh database or after pulling new migrations, apply the existing files:

```bash
python -m alembic upgrade head
python -m alembic current
```

The initial `create tenders table` migration is already included; there is no
need to generate it again during setup.

After changing ORM models, first ensure the database is at the current revision,
then generate a new migration:

```bash
python -m alembic upgrade head
python -m alembic revision --autogenerate -m "describe schema change"
```

Review the generated file in `backend/alembic/versions/`, including its
`upgrade()` and `downgrade()` operations, before applying it:

```bash
python -m alembic upgrade head
```

Commit migration files alongside the corresponding model changes. To view
migration history:

```bash
python -m alembic history
```

To undo the latest migration locally, review its `downgrade()` first because
it may remove tables or data, then run:

```bash
python -m alembic downgrade -1
```
