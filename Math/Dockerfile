# =========================
# 1) Build Stage
# =========================
FROM python:3.12-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Build dependencies (nur hier!)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    gfortran \
    libopenblas-dev \
    liblapack-dev \
    && rm -rf /var/lib/apt/lists/*

# Arbeitsverzeichnis
WORKDIR /install

# requirements zuerst (Caching Vorteil)
COPY requirements.txt .

# venv erstellen (best practice für multi-stage)
RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt


# =========================
# 2) Runtime Stage
# =========================
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# nur Runtime libs (kein gcc etc mehr!)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libopenblas0 \
    liblapack3 \
    && rm -rf /var/lib/apt/lists/*

# venv aus builder übernehmen
COPY --from=builder /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

# App
WORKDIR /app
COPY . /app

CMD ["python3", "headerTest.py", "./data/temp/session 2/*.csv"]