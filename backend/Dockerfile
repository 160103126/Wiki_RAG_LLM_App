# Build stage
FROM python:3.10-slim as builder

WORKDIR /app
COPY requirements/base.txt .

RUN pip install --user --no-cache-dir -r base.txt

# Runtime stage
FROM python:3.10-slim

WORKDIR /app

# Copy installed packages from builder
ENV PATH=/root/.local/bin:$PATH
COPY --from=builder /root/.local /root/.local

# Copy application code
COPY ./app ./app
COPY ./alembic.ini .
COPY ./alembic ./alembic

# Install production dependencies
RUN pip install --no-cache-dir gunicorn uvloop httptools

# Environment variables
ENV PYTHONPATH=/app \
    APP_ENV=prod \
    GUNICORN_WORKER_CLASS=uvicorn.workers.UvicornWorker \
    GUNICORN_WORKERS=4

# Database migration and startup command
CMD sh -c "alembic upgrade head && gunicorn app.main:app --workers $GUNICORN_WORKERS --worker-class $GUNICORN_WORKER_CLASS --bind 0.0.0.0:8000"