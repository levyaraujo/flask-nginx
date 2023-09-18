FROM python:3.11.5-alpine

WORKDIR /app

RUN apk add --no-cache build-base libffi-dev openssl-dev

RUN pip install poetry

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && poetry install --no-dev

COPY . .

# Run Gunicorn without the virtual environment
CMD gunicorn --bind 0.0.0.0:5000 "app:create_app()"
