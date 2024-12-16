FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN opentelemetry-bootstrap --action=install

EXPOSE 8080

CMD ["opentelemetry-instrument", "python3", "main.py"]
