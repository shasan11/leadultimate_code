#!/usr/bin/env python

from celery import Celery

# Create a Celery instance
app = Celery('mainsite', broker='redis://Z25I6CtyudX4Ajw5yNR@127.0.0.1:46415/0')

# Define a task
@app.task
def my_task():
    print('Running my_task')

# Start the Celery worker
if __name__ == '__main__':
    app.worker_main(['worker', '--loglevel=info','--concurrency=9'])
