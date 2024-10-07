FROM python:3.12.7-alpine AS builder
RUN pip install --upgrade poetry
COPY pyproject.toml poetry.lock /
RUN poetry export --only main -o /tmp/requirements.txt --without-hashes

# App
FROM python:3.12.7-alpine AS app

RUN pip3 install -U pip setuptools wheel

# Copy Python dependencies from the builder stage
COPY --from=builder /tmp/requirements.txt /tmp/requirements.txt

# Install Poetry dependencies
RUN pip3 install -r /tmp/requirements.txt

COPY src /src
WORKDIR /src
EXPOSE 8000
