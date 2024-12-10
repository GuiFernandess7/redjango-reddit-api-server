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

COPY requirements.txt .

RUN pip install uv

RUN uv venv /venv && \
    . /venv/bin/activate && \
    uv pip install -r requirements.txt

COPY . .

ENV PATH="/venv/bin:$PATH"

EXPOSE 8000

CMD ["python", "redjango/manage.py", "runserver", "0.0.0.0:8000"]