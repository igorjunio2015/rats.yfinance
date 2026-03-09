# rats.yfinance — Finance Data API

## Tech Stack
- Python 3.12
- FastAPI
- yfinance (Yahoo Finance data)
- Pydantic for validation
- pandas for data processing

## Commands
- `pip install -r requirements.txt` — Install dependencies
- `uvicorn main:app --reload` — Development server
- `python -m pytest test_example.py -v` — Run tests
- `docker-compose up` — Run with Docker

## Directory Structure
- `main.py` — FastAPI application entry point
- `app/` — Application package
  - `core/` — Configuration, settings
  - `routers/` — API route handlers
  - `schemas/` — Pydantic models
  - `services/` — Business logic
- `test_example.py` — Tests

## Rules
- All public functions must have type hints
- All endpoints must use Pydantic schemas for input/output
- No hardcoded API keys or secrets
- Audit logging for all data-fetching operations
- Pin all dependency versions in requirements.txt
