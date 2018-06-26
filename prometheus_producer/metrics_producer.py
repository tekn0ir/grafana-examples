from prometheus_client import start_http_server, Summary, Gauge
import random
import time
import math

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
metrics = {"pew": 0.0, "mew": 0.0, "dew": 0.0, "few": 0.0, "new": 0.0, "sew": 0.0}

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

def random_walk(metric):
    metrics[metric] += math.sin((random.randint(0, 9999)/10000.0) * math.pi * 2.0)
    return metrics[metric]

if __name__ == '__main__':
    pew = Gauge('pew', 'Prometheus metric')
    pew.set_function(lambda: random_walk('pew'))
    mew = Gauge('mew', 'Prometheus metric')
    mew.set_function(lambda: random_walk('mew'))
    dew = Gauge('dew', 'Prometheus metric')
    dew.set_function(lambda: random_walk('dew'))
    few = Gauge('few', 'Prometheus metric')
    few.set_function(lambda: random_walk('few'))
    new = Gauge('new', 'Prometheus metric')
    new.set_function(lambda: random_walk('new'))
    sew = Gauge('sew', 'Prometheus metric')
    sew.set_function(lambda: random_walk('sew'))
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        process_request(random.random())
