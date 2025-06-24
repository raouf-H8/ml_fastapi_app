FROM python:3.10-slim

WORKDIR /app
ENV PYTHONPATH=/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY model.pkl .
COPY app/ app/
COPY tests/ tests/

EXPOSE 8000

CMD ["sh", "-c", "sleep 5 && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
