from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

import time

@app.task
def add(x, y):
    time.sleep(1)
    return x + y

@app.task
def minus(x,y):
    time.sleep(1)
    return x-y