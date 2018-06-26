FROM python

RUN pip install --no-cache-dir prometheus_client
WORKDIR /app
COPY metrics_producer.py /app
ENTRYPOINT python metrics_producer.py
