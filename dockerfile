FROM ubuntu:24.04


RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    python3-venv \
    libpq-dev \
    postgresql \
    postgresql-contrib \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/pip install --upgrade pip


WORKDIR /app
COPY requirements.txt .
RUN /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

COPY ./services/ ./services/
COPY ./db/ ./db/
COPY ./config/ ./config/

ENV PATH="/opt/venv/bin:$PATH"

ENV PYTHONPATH="/app:/app/db"

RUN ls -la /app/services/

CMD ["python", "/app/services/server.py"]
