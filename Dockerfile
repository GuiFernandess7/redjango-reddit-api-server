FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV UV_SYSTEM_PYTHON=false

RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

ENV PATH="/root/.cargo/bin:${PATH}"

WORKDIR /app

COPY . .

RUN pip install uv

RUN uv venv /venv && \
    . /venv/bin/activate && \
    uv pip install .

COPY start.sh /start.sh
RUN chmod +x /start.sh

ENV PATH="/venv/bin:$PATH"

EXPOSE 8000

CMD ["./start.sh"]
