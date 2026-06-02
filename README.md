# Helping-backend

> ⚠️ Work in progress — early stage.

The backend service for the [Helping](https://github.com/TomerTasa100/Helping) app. A minimal **FastAPI** server that currently exposes a health check and a placeholder `/login` endpoint.

> [TODO] Tomer — describe the intended backend functionality once it grows beyond the login stub.

## Tech stack

Python · FastAPI · Uvicorn · Pydantic

## Setup & run

```bash
pip install fastapi uvicorn
uvicorn main:app --reload    # http://localhost:8000
```

API docs are auto-generated at `http://localhost:8000/docs`.

## Endpoints

| Method | Path | Description |
|---|---|---|
| `GET` | `/` | Health check — returns `{"status": "Online"}` |
| `POST` | `/login` | Placeholder auth — accepts `{username, password}` |

> ⚠️ **Note:** `/login` currently uses a hardcoded placeholder credential for local testing only. Replace it with real authentication before any real use. [TODO]
