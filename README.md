# Task Manager API

A FastAPI-based task management system with background processing capabilities.

## Features

- ✅ Create, read, update, delete tasks
- ✅ Task filtering and pagination
- ✅ Background task processing
- ✅ Async database operations with SQLAlchemy
- ✅ Database migrations with Alembic
- ✅ Comprehensive test suite
- ✅ Docker support

## Quick Start

### 1. Set up Environment

```bash
cp .env.example .env
# Edit .env with your configuration
```

### 2. Start with Docker

```bash
docker-compose up -d
```

### 3. Run Database Migrations

```bash
# If using Docker
docker-compose run --rm migrations

# If running locally
alembic upgrade head
```

### 4. Access the API

- API: http://localhost:8000
- Documentation: http://localhost:8000/docs
- Alternative docs: http://localhost:8000/redoc

## Development

### Running Locally

```bash
# Start the API server
uvicorn app.main:app --reload

# Start the background worker
python -m app.worker
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test file
pytest tests/api/test_tasks.py
```

### Database Migrations

```bash
# Create a new migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Revert migration
alembic downgrade -1
```

## API Endpoints

- `POST /api/v1/tasks/` - Create a new task
- `GET /api/v1/tasks/` - List tasks (with filtering and pagination)
- `GET /api/v1/tasks/{task_id}` - Get task by ID
- `PUT /api/v1/tasks/{task_id}` - Update task
- `DELETE /api/v1/tasks/{task_id}` - Delete task
- `POST /api/v1/tasks/{task_id}/process` - Start background processing

## Project Structure

- `app/` - Main application code
  - `api/` - API routes and endpoints
  - `models/` - SQLAlchemy database models
  - `schemas/` - Pydantic request/response schemas
  - `crud/` - Database operations
  - `services/` - Business logic
  - `background/` - Background task definitions
- `tests/` - Test suite
- `alembic/` - Database migrations

## Docker

See `docker-compose.yml` for the complete containerized setup including:
- FastAPI application
- PostgreSQL database
- Redis for task queuing
- Background worker
- Database migrations
