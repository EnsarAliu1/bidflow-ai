# BidFlow AI

Backend built with Python and FastAPI.

## Requirements

- Python 3.10 or newer
- Bash terminal (Git Bash on Windows)
- Docker with Docker Compose (Docker Desktop on Windows)

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
