FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PYTHONUNBUFFERED=1

WORKDIR /producer

# Install packages without actually copying in app code
COPY uv.lock pyproject.toml .
RUN uv sync --frozen --no-install-project

# Copy app code and finish UV project setup
COPY . .
RUN uv sync --frozen 

CMD ["uv", "run", "python", "main.py"]
