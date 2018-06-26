FROM python:3.7-rc-slim

RUN pip install --no-cache-dir clickhouse
WORKDIR /app
COPY metrics_producer.py /app
ENTRYPOINT python metrics_producer.py
