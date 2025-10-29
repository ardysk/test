FROM python:3.12-slim

WORKDIR /app
COPY app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY app /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Uvicorn logs go to stdout/stderr for Loki/Promtail
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
