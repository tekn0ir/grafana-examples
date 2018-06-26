#!/bin/env python

import requests
import random
import math
import time
import sys
import traceback
import logging

def main():
    time.sleep(4.15)
    while True:
        try:
            metrics = {"pew": 0.0, "mew": 0.0, "dew": 0.0, "few": 0.0, "new": 0.0, "sew": 0.0}
            while True:
                metric = random.choice(list(metrics.keys()))
                metrics[metric] += math.sin((random.randint(0, 9999)/10000.0) * math.pi * 2)
                data = 'influxdb_metric,host=influxdb_producer,tag=' + metric + ' value=' + str(metrics[metric]) + ' ' + str(time.time_ns())
                print(data)
                sys.stdout.flush()
                r = requests.post(url='http://influxdb:8086/write?db=test', data=data, headers={'Content-Type': 'application/octet-stream'})
                print(r)
                sys.stdout.flush()
                time.sleep(0.15)
        except:
            logging.error(traceback.format_exc())
            time.sleep(1)
            continue

if __name__ == '__main__':
    main()

# curl -G http://influxdb:8086/query --data-urlencode "q=CREATE DATABASE mydb" |
# curl -i -XPOST 'http://influxdb:8086/write?db=mydb' --data-binary 'cpu_load_short,host=server01,region=us-west value=0.64 1434055562000000000'
