#!/bin/env python

import random
import math
import time
import sys
import traceback
import logging

from datetime import date, datetime
from clickhouse.database import Database
from clickhouse.engines import MergeTree
from clickhouse.fields import DateField, DateTimeField, Float32Field, StringField
from clickhouse.models import Model

class Metrics(Model):
    Name = StringField()
    PartitionDate = DateField()
    Time = DateTimeField()
    Value = Float32Field()
    engine = MergeTree('PartitionDate', ('Name', 'PartitionDate'))

def main():
    time.sleep(10.0)
    while True:
        try:
            db = Database('clickhouse:8123', 'default')
            metrics = {"pew": 0.0, "mew": 0.0, "dew": 0.0, "few": 0.0, "new": 0.0, "sew": 0.0}
            while True:
                metric = random.choice(list(metrics.keys()))
                metrics[metric] += math.sin((random.randint(0, 9999)/10000.0) * math.pi * 2)
                m = Metrics(Name=metric, Time=datetime.now(), PartitionDate=date.today().isoformat(), Value=metrics[metric])
                print(m)
                sys.stdout.flush()
                db.insert([m])
                time.sleep(0.15)
        except:
            logging.error(traceback.format_exc())
            time.sleep(1)
            continue

if __name__ == '__main__':
    main()